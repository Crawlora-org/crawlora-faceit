require "json"
require "net/http"
require "uri"

module Crawlora
  module Faceit
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"faceit-ban-reasons": {"bodyParam": null, "bodyRequired": false, "id": "faceit-ban-reasons", "method": "GET", "params": [], "path": "/faceit/ban-reasons", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "faceit-banlist": {"bodyParam": null, "bodyRequired": false, "id": "faceit-banlist", "method": "GET", "params": [{"description": "Optional page size, 5-100; default 25.", "in": "query", "name": "size", "type": "integer", "x-example": 25}, {"description": "Optional opaque cursor copied from the previous response; omit for the first page.", "in": "query", "name": "cursor", "type": "string"}, {"description": "Optional ban reason, one of: ban evasion, cheating, multiple accounts, platform abuse, smurfing, toxicity, playing on a smurf (see faceit-ban-reasons).", "in": "query", "name": "reason", "type": "string", "x-example": "toxicity"}], "path": "/faceit/banlist", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "size", "type": "integer"}, {"in": "query", "name": "cursor", "type": "string"}, {"in": "query", "name": "reason", "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-banlist-stats": {"bodyParam": null, "bodyRequired": false, "id": "faceit-banlist-stats", "method": "GET", "params": [], "path": "/faceit/banlist-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "faceit-best-clips": {"bodyParam": null, "bodyRequired": false, "id": "faceit-best-clips", "method": "GET", "params": [{"description": "Game slug; only cs2 has Allstar clips.", "enum": ["cs2"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2"}, {"description": "FACEIT user UUID.", "in": "query", "name": "user_id", "required": true, "type": "string", "x-example": "74df0e6b-5b41-42d7-93b4-05dc78b9a699"}, {"description": "Inclusive lower bound as an RFC3339 timestamp.", "in": "query", "name": "from", "required": true, "type": "string", "x-example": "2026-01-01T00:00:00Z"}, {"description": "Inclusive upper bound as an RFC3339 timestamp.", "in": "query", "name": "to", "required": true, "type": "string", "x-example": "2026-11-10T00:00:00Z"}, {"description": "Optional page size, 1-100; default 10.", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/faceit/best-clips", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "user_id", "required": true, "type": "string"}, {"in": "query", "name": "from", "required": true, "type": "string"}, {"in": "query", "name": "to", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-championship": {"bodyParam": null, "bodyRequired": false, "id": "faceit-championship", "method": "GET", "params": [{"description": "Championship UUID from faceit-championship-search.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "9888a3f4-e292-4c3a-a511-15d5d2fb112b"}], "path": "/faceit/championship", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-championship-bracket": {"bodyParam": null, "bodyRequired": false, "id": "faceit-championship-bracket", "method": "GET", "params": [{"description": "Championship UUID from faceit-championship-search.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "9888a3f4-e292-4c3a-a511-15d5d2fb112b"}, {"description": "Group number.", "in": "query", "name": "group", "required": true, "type": "integer", "x-example": 1}, {"description": "Round number.", "in": "query", "name": "round", "required": true, "type": "integer", "x-example": 1}, {"description": "Optional non-negative start offset.", "in": "query", "name": "start", "type": "integer", "x-example": 0}, {"description": "Optional end offset.", "in": "query", "name": "end", "type": "integer", "x-example": 50}], "path": "/faceit/championship-bracket", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "group", "required": true, "type": "integer"}, {"in": "query", "name": "round", "required": true, "type": "integer"}, {"in": "query", "name": "start", "type": "integer"}, {"in": "query", "name": "end", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-championship-participants": {"bodyParam": null, "bodyRequired": false, "id": "faceit-championship-participants", "method": "GET", "params": [{"description": "Championship UUID from faceit-championship-search.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "9888a3f4-e292-4c3a-a511-15d5d2fb112b"}, {"description": "Optional page size, 1-50; default 20.", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/championship-participants", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-championship-search": {"bodyParam": null, "bodyRequired": false, "id": "faceit-championship-search", "method": "GET", "params": [{"description": "Optional entity type; defaults to championship. Documented values: championship, hub, tournament, league, club, matchmaking.", "in": "query", "name": "entity_type", "type": "string", "x-example": "championship"}, {"description": "Optional leaderboard type; defaults to championship and normally equals entity_type.", "in": "query", "name": "type", "type": "string", "x-example": "championship"}, {"description": "Optional status, one of ONGOING, UPCOMING or FINISHED; defaults to ONGOING.", "enum": ["ONGOING", "UPCOMING", "FINISHED"], "in": "query", "name": "status", "type": "string", "x-example": "ONGOING"}, {"description": "Optional leaderboard subtype filter.", "in": "query", "name": "subtype", "type": "string"}, {"description": "Optional two-letter ISO country code such as DE.", "in": "query", "name": "country", "type": "string", "x-example": "DE"}, {"description": "Optional game slug, one of the values returned by faceit-games.", "enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}, {"description": "Optional drops filter.", "in": "query", "name": "has_drops", "type": "boolean", "x-example": true}, {"description": "Optional page size, 1-100; default 25.", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/championship-search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "entity_type", "type": "string"}, {"in": "query", "name": "type", "type": "string"}, {"enum": ["ONGOING", "UPCOMING", "FINISHED"], "in": "query", "name": "status", "type": "string"}, {"in": "query", "name": "subtype", "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "has_drops", "type": "boolean"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-clip": {"bodyParam": null, "bodyRequired": false, "id": "faceit-clip", "method": "GET", "params": [{"description": "24-character clip id from faceit-clips.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "6a57e63f8d9a5a0549f503c8"}], "path": "/faceit/clip", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-clips": {"bodyParam": null, "bodyRequired": false, "id": "faceit-clips", "method": "GET", "params": [{"description": "Game slug; only cs2 has Allstar clips.", "enum": ["cs2"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}, {"description": "FACEIT user UUID.", "in": "query", "name": "user_id", "required": true, "type": "string", "x-example": "74df0e6b-5b41-42d7-93b4-05dc78b9a699"}, {"description": "Optional page size, 1-100; default 10.", "in": "query", "name": "limit", "type": "integer", "x-example": 10}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/clips", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "user_id", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-competition-matches": {"bodyParam": null, "bodyRequired": false, "id": "faceit-competition-matches", "method": "GET", "params": [{"description": "Competition id from faceit-championship-search.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "9888a3f4-e292-4c3a-a511-15d5d2fb112b"}, {"description": "Competition type such as championship; the upstream rejects a missing type.", "in": "query", "name": "type", "required": true, "type": "string", "x-example": "championship"}, {"description": "Optional player UUID filter.", "in": "query", "name": "player_id", "type": "string", "x-example": "74df0e6b-5b41-42d7-93b4-05dc78b9a699"}, {"description": "Optional non-negative page number; default 0.", "in": "query", "name": "page", "type": "integer", "x-example": 0}, {"description": "Optional page size, 1-100; default 20.", "in": "query", "name": "size", "type": "integer", "x-example": 20}], "path": "/faceit/competition-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "type", "required": true, "type": "string"}, {"in": "query", "name": "player_id", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-fpl": {"bodyParam": null, "bodyRequired": false, "id": "faceit-fpl", "method": "GET", "params": [{"description": "Optional game slug, one of the values returned by faceit-games.", "enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}, {"description": "Optional page size, 1-100; default 20.", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/fpl", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-game-modes": {"bodyParam": null, "bodyRequired": false, "id": "faceit-game-modes", "method": "GET", "params": [{"description": "Game slug, one of the values returned by faceit-games.", "enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}, {"description": "Region code such as EU; see faceit-regions.", "in": "query", "name": "region", "required": true, "type": "string", "x-example": "EU"}], "path": "/faceit/game-modes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "region", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-games": {"bodyParam": null, "bodyRequired": false, "id": "faceit-games", "method": "GET", "params": [], "path": "/faceit/games", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "faceit-hub": {"bodyParam": null, "bodyRequired": false, "id": "faceit-hub", "method": "GET", "params": [{"description": "Hub UUID from faceit-hub-memberships.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "27ccb2d1-2715-4f65-be3f-c5de635fcd31"}], "path": "/faceit/hub", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-hub-categories": {"bodyParam": null, "bodyRequired": false, "id": "faceit-hub-categories", "method": "GET", "params": [], "path": "/faceit/hub-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "faceit-hub-memberships": {"bodyParam": null, "bodyRequired": false, "id": "faceit-hub-memberships", "method": "GET", "params": [{"description": "FACEIT user UUID.", "in": "query", "name": "user_id", "required": true, "type": "string", "x-example": "74df0e6b-5b41-42d7-93b4-05dc78b9a699"}, {"description": "Optional hub category; one of community, chat or ihl.", "enum": ["community", "chat", "ihl"], "in": "query", "name": "category", "type": "string", "x-example": "community"}, {"description": "Optional page size, 1-50; default 20.", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/hub-memberships", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "user_id", "required": true, "type": "string"}, {"enum": ["community", "chat", "ihl"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-hubs": {"bodyParam": null, "bodyRequired": false, "id": "faceit-hubs", "method": "GET", "params": [{"collectionFormat": "multi", "description": "Hub UUIDs; repeat the parameter for up to 20 hubs.", "in": "query", "items": {"type": "string"}, "name": "ids", "required": true, "type": "array", "x-example": "27ccb2d1-2715-4f65-be3f-c5de635fcd31"}], "path": "/faceit/hubs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"collectionFormat": "multi", "in": "query", "name": "ids", "required": true, "type": "array"}], "security": ["ApiKeyAuth"]}, "faceit-hubs-detailed": {"bodyParam": null, "bodyRequired": false, "id": "faceit-hubs-detailed", "method": "GET", "params": [{"collectionFormat": "multi", "description": "Hub UUIDs; repeat the parameter for up to 20 hubs.", "in": "query", "items": {"type": "string"}, "name": "ids", "required": true, "type": "array", "x-example": "27ccb2d1-2715-4f65-be3f-c5de635fcd31"}], "path": "/faceit/hubs-detailed", "pathParams": [], "produces": ["application/json"], "queryParams": [{"collectionFormat": "multi", "in": "query", "name": "ids", "required": true, "type": "array"}], "security": ["ApiKeyAuth"]}, "faceit-leaderboard": {"bodyParam": null, "bodyRequired": false, "id": "faceit-leaderboard", "method": "GET", "params": [{"description": "Game slug, one of the values returned by faceit-games.", "enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}, {"description": "Region code such as EU or NA; see faceit-regions.", "in": "query", "name": "region", "required": true, "type": "string", "x-example": "EU"}, {"description": "Optional season number; when set the season-aware ranking is read.", "in": "query", "name": "season", "type": "integer", "x-example": 10}, {"description": "Optional page size, 1-100; default 20 and the gateway caps a page at 100 rows.", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/leaderboard", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "region", "required": true, "type": "string"}, {"in": "query", "name": "season", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-leaderboard-detail": {"bodyParam": null, "bodyRequired": false, "id": "faceit-leaderboard-detail", "method": "GET", "params": [{"description": "24-character leaderboard id from faceit-championship-search or faceit-standings.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "5b0d895ef2e59b000687c9ed"}], "path": "/faceit/leaderboard-detail", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-leaderboard-statuses": {"bodyParam": null, "bodyRequired": false, "id": "faceit-leaderboard-statuses", "method": "GET", "params": [], "path": "/faceit/leaderboard-statuses", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "faceit-maps": {"bodyParam": null, "bodyRequired": false, "id": "faceit-maps", "method": "GET", "params": [{"description": "Game slug, one of the values returned by faceit-games.", "enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}], "path": "/faceit/maps", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-match-clips": {"bodyParam": null, "bodyRequired": false, "id": "faceit-match-clips", "method": "GET", "params": [{"description": "Game slug; only cs2 has Allstar clips.", "enum": ["cs2"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2"}, {"description": "Upstream match id from a clip row, for example 1-bef84e57-4ce3-41aa-b5e5-2918228c1c28.", "in": "query", "name": "match_id", "required": true, "type": "string", "x-example": "1-bef84e57-4ce3-41aa-b5e5-2918228c1c28"}, {"description": "Optional page size, 1-100; default 10.", "in": "query", "name": "limit", "type": "integer", "x-example": 10}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/match-clips", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "match_id", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-organizer": {"bodyParam": null, "bodyRequired": false, "id": "faceit-organizer", "method": "GET", "params": [{"description": "Organizer UUID.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "73d4185d-559f-4dbc-8398-9eae47adfe27"}], "path": "/faceit/organizer", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-player": {"bodyParam": null, "bodyRequired": false, "id": "faceit-player", "method": "GET", "params": [{"description": "Optional FACEIT nickname; exactly one of nickname and user_id is required.", "in": "query", "name": "nickname", "type": "string", "x-example": "dem0nnnnnnnn"}, {"description": "Optional FACEIT user UUID; exactly one of nickname and user_id is required.", "in": "query", "name": "user_id", "type": "string", "x-example": "74df0e6b-5b41-42d7-93b4-05dc78b9a699"}], "path": "/faceit/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "nickname", "type": "string"}, {"in": "query", "name": "user_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-player-rank": {"bodyParam": null, "bodyRequired": false, "id": "faceit-player-rank", "method": "GET", "params": [{"description": "Game slug, one of the values returned by faceit-games.", "enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}, {"description": "Region code such as EU or NA; see faceit-regions for the documented values.", "in": "query", "name": "region", "required": true, "type": "string", "x-example": "EU"}, {"description": "Optional FACEIT nickname; exactly one of nickname and user_id is required.", "in": "query", "name": "nickname", "type": "string", "x-example": "dem0nnnnnnnn"}, {"description": "Optional FACEIT user UUID; exactly one of nickname and user_id is required.", "in": "query", "name": "user_id", "type": "string", "x-example": "74df0e6b-5b41-42d7-93b4-05dc78b9a699"}, {"description": "Optional season number; when set the season-aware ranking is read.", "in": "query", "name": "season", "type": "integer", "x-example": 10}], "path": "/faceit/player-rank", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "region", "required": true, "type": "string"}, {"in": "query", "name": "nickname", "type": "string"}, {"in": "query", "name": "user_id", "type": "string"}, {"in": "query", "name": "season", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-regions": {"bodyParam": null, "bodyRequired": false, "id": "faceit-regions", "method": "GET", "params": [], "path": "/faceit/regions", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "faceit-rule": {"bodyParam": null, "bodyRequired": false, "id": "faceit-rule", "method": "GET", "params": [{"description": "Rule UUID from faceit-rules.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "43e07c2c-c0b2-4872-9826-6812eba70463"}], "path": "/faceit/rule", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-rules": {"bodyParam": null, "bodyRequired": false, "id": "faceit-rules", "method": "GET", "params": [{"description": "Optional page size, 1-100; default 20.", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/rules", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-skill-levels": {"bodyParam": null, "bodyRequired": false, "id": "faceit-skill-levels", "method": "GET", "params": [{"description": "Game slug, one of the values returned by faceit-games.", "enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}], "path": "/faceit/skill-levels", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-standings": {"bodyParam": null, "bodyRequired": false, "id": "faceit-standings", "method": "GET", "params": [{"description": "Championship UUID from faceit-championship-search.", "in": "query", "name": "entity_id", "required": true, "type": "string", "x-example": "9888a3f4-e292-4c3a-a511-15d5d2fb112b"}, {"description": "Group number.", "in": "query", "name": "group", "required": true, "type": "integer", "x-example": 1}, {"description": "Round number, or a comma-separated list such as 1,2.", "in": "query", "name": "round", "required": true, "type": "string", "x-example": "1"}, {"description": "Optional segment number; provide segment or match.", "in": "query", "name": "segment", "type": "integer", "x-example": 1}, {"description": "Optional match number; provide segment or match.", "in": "query", "name": "match", "type": "integer", "x-example": 1}], "path": "/faceit/standings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "entity_id", "required": true, "type": "string"}, {"in": "query", "name": "group", "required": true, "type": "integer"}, {"in": "query", "name": "round", "required": true, "type": "string"}, {"in": "query", "name": "segment", "type": "integer"}, {"in": "query", "name": "match", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-team": {"bodyParam": null, "bodyRequired": false, "id": "faceit-team", "method": "GET", "params": [{"description": "Team UUID from a premade bracket faction id.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "3279bf46-2cd3-43d1-b4d7-2dfd24d1d843"}], "path": "/faceit/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-tournaments-past": {"bodyParam": null, "bodyRequired": false, "id": "faceit-tournaments-past", "method": "GET", "params": [{"description": "FACEIT nickname.", "in": "query", "name": "nickname", "required": true, "type": "string", "x-example": "dem0nnnnnnnn"}, {"description": "Optional page size, 1-100; default 20.", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/tournaments-past", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "nickname", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-user-skills": {"bodyParam": null, "bodyRequired": false, "id": "faceit-user-skills", "method": "GET", "params": [{"collectionFormat": "multi", "description": "Required FACEIT user UUIDs; repeat the parameter for up to 10 users.", "in": "query", "items": {"type": "string"}, "name": "user_ids", "required": true, "type": "array", "x-example": "74df0e6b-5b41-42d7-93b4-05dc78b9a699"}, {"description": "Game slug, one of the values returned by faceit-games.", "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}], "path": "/faceit/user-skills", "pathParams": [], "produces": ["application/json"], "queryParams": [{"collectionFormat": "multi", "in": "query", "name": "user_ids", "required": true, "type": "array"}, {"in": "query", "name": "game", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["faceit-ban-reasons", "faceit-banlist", "faceit-banlist-stats", "faceit-best-clips", "faceit-championship", "faceit-championship-bracket", "faceit-championship-participants", "faceit-championship-search", "faceit-clip", "faceit-clips", "faceit-competition-matches", "faceit-fpl", "faceit-game-modes", "faceit-games", "faceit-hub", "faceit-hub-categories", "faceit-hub-memberships", "faceit-hubs", "faceit-hubs-detailed", "faceit-leaderboard", "faceit-leaderboard-detail", "faceit-leaderboard-statuses", "faceit-maps", "faceit-match-clips", "faceit-organizer", "faceit-player", "faceit-player-rank", "faceit-regions", "faceit-rule", "faceit-rules", "faceit-skill-levels", "faceit-standings", "faceit-team", "faceit-tournaments-past", "faceit-user-skills"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-faceit-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('ban_reasons') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-ban-reasons', params, response_type: response_type)
      end
      define_method('banlist') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-banlist', params, response_type: response_type)
      end
      define_method('banlist_stats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-banlist-stats', params, response_type: response_type)
      end
      define_method('best_clips') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-best-clips', params, response_type: response_type)
      end
      define_method('championship') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-championship', params, response_type: response_type)
      end
      define_method('championship_bracket') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-championship-bracket', params, response_type: response_type)
      end
      define_method('championship_participants') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-championship-participants', params, response_type: response_type)
      end
      define_method('championship_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-championship-search', params, response_type: response_type)
      end
      define_method('clip') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-clip', params, response_type: response_type)
      end
      define_method('clips') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-clips', params, response_type: response_type)
      end
      define_method('competition_matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-competition-matches', params, response_type: response_type)
      end
      define_method('fpl') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-fpl', params, response_type: response_type)
      end
      define_method('game_modes') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-game-modes', params, response_type: response_type)
      end
      define_method('games') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-games', params, response_type: response_type)
      end
      define_method('hub') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-hub', params, response_type: response_type)
      end
      define_method('hub_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-hub-categories', params, response_type: response_type)
      end
      define_method('hub_memberships') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-hub-memberships', params, response_type: response_type)
      end
      define_method('hubs') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-hubs', params, response_type: response_type)
      end
      define_method('hubs_detailed') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-hubs-detailed', params, response_type: response_type)
      end
      define_method('leaderboard') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-leaderboard', params, response_type: response_type)
      end
      define_method('leaderboard_detail') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-leaderboard-detail', params, response_type: response_type)
      end
      define_method('leaderboard_statuses') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-leaderboard-statuses', params, response_type: response_type)
      end
      define_method('maps') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-maps', params, response_type: response_type)
      end
      define_method('match_clips') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-match-clips', params, response_type: response_type)
      end
      define_method('organizer') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-organizer', params, response_type: response_type)
      end
      define_method('player') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-player', params, response_type: response_type)
      end
      define_method('player_rank') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-player-rank', params, response_type: response_type)
      end
      define_method('regions') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-regions', params, response_type: response_type)
      end
      define_method('rule') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-rule', params, response_type: response_type)
      end
      define_method('rules') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-rules', params, response_type: response_type)
      end
      define_method('skill_levels') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-skill-levels', params, response_type: response_type)
      end
      define_method('standings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-standings', params, response_type: response_type)
      end
      define_method('team') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-team', params, response_type: response_type)
      end
      define_method('tournaments_past') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-tournaments-past', params, response_type: response_type)
      end
      define_method('user_skills') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('faceit-user-skills', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
