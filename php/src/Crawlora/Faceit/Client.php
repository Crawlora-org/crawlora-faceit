<?php

declare(strict_types=1);

namespace Crawlora\Faceit;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'faceit';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 35;
    public const OPERATION_IDS = ["faceit-ban-reasons", "faceit-banlist", "faceit-banlist-stats", "faceit-best-clips", "faceit-championship", "faceit-championship-bracket", "faceit-championship-participants", "faceit-championship-search", "faceit-clip", "faceit-clips", "faceit-competition-matches", "faceit-fpl", "faceit-game-modes", "faceit-games", "faceit-hub", "faceit-hub-categories", "faceit-hub-memberships", "faceit-hubs", "faceit-hubs-detailed", "faceit-leaderboard", "faceit-leaderboard-detail", "faceit-leaderboard-statuses", "faceit-maps", "faceit-match-clips", "faceit-organizer", "faceit-player", "faceit-player-rank", "faceit-regions", "faceit-rule", "faceit-rules", "faceit-skill-levels", "faceit-standings", "faceit-team", "faceit-tournaments-past", "faceit-user-skills"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"faceit-ban-reasons": {"bodyParam": null, "bodyRequired": false, "id": "faceit-ban-reasons", "method": "GET", "params": [], "path": "/faceit/ban-reasons", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "faceit-banlist": {"bodyParam": null, "bodyRequired": false, "id": "faceit-banlist", "method": "GET", "params": [{"description": "Optional page size, 5-100; default 25.", "in": "query", "name": "size", "type": "integer", "x-example": 25}, {"description": "Optional opaque cursor copied from the previous response; omit for the first page.", "in": "query", "name": "cursor", "type": "string"}, {"description": "Optional ban reason, one of: ban evasion, cheating, multiple accounts, platform abuse, smurfing, toxicity, playing on a smurf (see faceit-ban-reasons).", "in": "query", "name": "reason", "type": "string", "x-example": "toxicity"}], "path": "/faceit/banlist", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "size", "type": "integer"}, {"in": "query", "name": "cursor", "type": "string"}, {"in": "query", "name": "reason", "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-banlist-stats": {"bodyParam": null, "bodyRequired": false, "id": "faceit-banlist-stats", "method": "GET", "params": [], "path": "/faceit/banlist-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "faceit-best-clips": {"bodyParam": null, "bodyRequired": false, "id": "faceit-best-clips", "method": "GET", "params": [{"description": "Game slug; only cs2 has Allstar clips.", "enum": ["cs2"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2"}, {"description": "FACEIT user UUID.", "in": "query", "name": "user_id", "required": true, "type": "string", "x-example": "74df0e6b-5b41-42d7-93b4-05dc78b9a699"}, {"description": "Inclusive lower bound as an RFC3339 timestamp.", "in": "query", "name": "from", "required": true, "type": "string", "x-example": "2026-01-01T00:00:00Z"}, {"description": "Inclusive upper bound as an RFC3339 timestamp.", "in": "query", "name": "to", "required": true, "type": "string", "x-example": "2026-11-10T00:00:00Z"}, {"description": "Optional page size, 1-100; default 10.", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/faceit/best-clips", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "user_id", "required": true, "type": "string"}, {"in": "query", "name": "from", "required": true, "type": "string"}, {"in": "query", "name": "to", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-championship": {"bodyParam": null, "bodyRequired": false, "id": "faceit-championship", "method": "GET", "params": [{"description": "Championship UUID from faceit-championship-search.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "9888a3f4-e292-4c3a-a511-15d5d2fb112b"}], "path": "/faceit/championship", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-championship-bracket": {"bodyParam": null, "bodyRequired": false, "id": "faceit-championship-bracket", "method": "GET", "params": [{"description": "Championship UUID from faceit-championship-search.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "9888a3f4-e292-4c3a-a511-15d5d2fb112b"}, {"description": "Group number.", "in": "query", "name": "group", "required": true, "type": "integer", "x-example": 1}, {"description": "Round number.", "in": "query", "name": "round", "required": true, "type": "integer", "x-example": 1}, {"description": "Optional non-negative start offset.", "in": "query", "name": "start", "type": "integer", "x-example": 0}, {"description": "Optional end offset.", "in": "query", "name": "end", "type": "integer", "x-example": 50}], "path": "/faceit/championship-bracket", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "group", "required": true, "type": "integer"}, {"in": "query", "name": "round", "required": true, "type": "integer"}, {"in": "query", "name": "start", "type": "integer"}, {"in": "query", "name": "end", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-championship-participants": {"bodyParam": null, "bodyRequired": false, "id": "faceit-championship-participants", "method": "GET", "params": [{"description": "Championship UUID from faceit-championship-search.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "9888a3f4-e292-4c3a-a511-15d5d2fb112b"}, {"description": "Optional page size, 1-50; default 20.", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/championship-participants", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-championship-search": {"bodyParam": null, "bodyRequired": false, "id": "faceit-championship-search", "method": "GET", "params": [{"description": "Optional entity type; defaults to championship. Documented values: championship, hub, tournament, league, club, matchmaking.", "in": "query", "name": "entity_type", "type": "string", "x-example": "championship"}, {"description": "Optional leaderboard type; defaults to championship and normally equals entity_type.", "in": "query", "name": "type", "type": "string", "x-example": "championship"}, {"description": "Optional status, one of ONGOING, UPCOMING or FINISHED; defaults to ONGOING.", "enum": ["ONGOING", "UPCOMING", "FINISHED"], "in": "query", "name": "status", "type": "string", "x-example": "ONGOING"}, {"description": "Optional leaderboard subtype filter.", "in": "query", "name": "subtype", "type": "string"}, {"description": "Optional two-letter ISO country code such as DE.", "in": "query", "name": "country", "type": "string", "x-example": "DE"}, {"description": "Optional game slug, one of the values returned by faceit-games.", "enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}, {"description": "Optional drops filter.", "in": "query", "name": "has_drops", "type": "boolean", "x-example": true}, {"description": "Optional page size, 1-100; default 25.", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/championship-search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "entity_type", "type": "string"}, {"in": "query", "name": "type", "type": "string"}, {"enum": ["ONGOING", "UPCOMING", "FINISHED"], "in": "query", "name": "status", "type": "string"}, {"in": "query", "name": "subtype", "type": "string"}, {"in": "query", "name": "country", "type": "string"}, {"enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "has_drops", "type": "boolean"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-clip": {"bodyParam": null, "bodyRequired": false, "id": "faceit-clip", "method": "GET", "params": [{"description": "24-character clip id from faceit-clips.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "6a57e63f8d9a5a0549f503c8"}], "path": "/faceit/clip", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-clips": {"bodyParam": null, "bodyRequired": false, "id": "faceit-clips", "method": "GET", "params": [{"description": "Game slug; only cs2 has Allstar clips.", "enum": ["cs2"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}, {"description": "FACEIT user UUID.", "in": "query", "name": "user_id", "required": true, "type": "string", "x-example": "74df0e6b-5b41-42d7-93b4-05dc78b9a699"}, {"description": "Optional page size, 1-100; default 10.", "in": "query", "name": "limit", "type": "integer", "x-example": 10}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/clips", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "user_id", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-competition-matches": {"bodyParam": null, "bodyRequired": false, "id": "faceit-competition-matches", "method": "GET", "params": [{"description": "Competition id from faceit-championship-search.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "9888a3f4-e292-4c3a-a511-15d5d2fb112b"}, {"description": "Competition type such as championship; the upstream rejects a missing type.", "in": "query", "name": "type", "required": true, "type": "string", "x-example": "championship"}, {"description": "Optional player UUID filter.", "in": "query", "name": "player_id", "type": "string", "x-example": "74df0e6b-5b41-42d7-93b4-05dc78b9a699"}, {"description": "Optional non-negative page number; default 0.", "in": "query", "name": "page", "type": "integer", "x-example": 0}, {"description": "Optional page size, 1-100; default 20.", "in": "query", "name": "size", "type": "integer", "x-example": 20}], "path": "/faceit/competition-matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "type", "required": true, "type": "string"}, {"in": "query", "name": "player_id", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-fpl": {"bodyParam": null, "bodyRequired": false, "id": "faceit-fpl", "method": "GET", "params": [{"description": "Optional game slug, one of the values returned by faceit-games.", "enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}, {"description": "Optional page size, 1-100; default 20.", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/fpl", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-game-modes": {"bodyParam": null, "bodyRequired": false, "id": "faceit-game-modes", "method": "GET", "params": [{"description": "Game slug, one of the values returned by faceit-games.", "enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}, {"description": "Region code such as EU; see faceit-regions.", "in": "query", "name": "region", "required": true, "type": "string", "x-example": "EU"}], "path": "/faceit/game-modes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "region", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-games": {"bodyParam": null, "bodyRequired": false, "id": "faceit-games", "method": "GET", "params": [], "path": "/faceit/games", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "faceit-hub": {"bodyParam": null, "bodyRequired": false, "id": "faceit-hub", "method": "GET", "params": [{"description": "Hub UUID from faceit-hub-memberships.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "27ccb2d1-2715-4f65-be3f-c5de635fcd31"}], "path": "/faceit/hub", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-hub-categories": {"bodyParam": null, "bodyRequired": false, "id": "faceit-hub-categories", "method": "GET", "params": [], "path": "/faceit/hub-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "faceit-hub-memberships": {"bodyParam": null, "bodyRequired": false, "id": "faceit-hub-memberships", "method": "GET", "params": [{"description": "FACEIT user UUID.", "in": "query", "name": "user_id", "required": true, "type": "string", "x-example": "74df0e6b-5b41-42d7-93b4-05dc78b9a699"}, {"description": "Optional hub category; one of community, chat or ihl.", "enum": ["community", "chat", "ihl"], "in": "query", "name": "category", "type": "string", "x-example": "community"}, {"description": "Optional page size, 1-50; default 20.", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/hub-memberships", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "user_id", "required": true, "type": "string"}, {"enum": ["community", "chat", "ihl"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-hubs": {"bodyParam": null, "bodyRequired": false, "id": "faceit-hubs", "method": "GET", "params": [{"collectionFormat": "multi", "description": "Hub UUIDs; repeat the parameter for up to 20 hubs.", "in": "query", "items": {"type": "string"}, "name": "ids", "required": true, "type": "array", "x-example": "27ccb2d1-2715-4f65-be3f-c5de635fcd31"}], "path": "/faceit/hubs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"collectionFormat": "multi", "in": "query", "name": "ids", "required": true, "type": "array"}], "security": ["ApiKeyAuth"]}, "faceit-hubs-detailed": {"bodyParam": null, "bodyRequired": false, "id": "faceit-hubs-detailed", "method": "GET", "params": [{"collectionFormat": "multi", "description": "Hub UUIDs; repeat the parameter for up to 20 hubs.", "in": "query", "items": {"type": "string"}, "name": "ids", "required": true, "type": "array", "x-example": "27ccb2d1-2715-4f65-be3f-c5de635fcd31"}], "path": "/faceit/hubs-detailed", "pathParams": [], "produces": ["application/json"], "queryParams": [{"collectionFormat": "multi", "in": "query", "name": "ids", "required": true, "type": "array"}], "security": ["ApiKeyAuth"]}, "faceit-leaderboard": {"bodyParam": null, "bodyRequired": false, "id": "faceit-leaderboard", "method": "GET", "params": [{"description": "Game slug, one of the values returned by faceit-games.", "enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}, {"description": "Region code such as EU or NA; see faceit-regions.", "in": "query", "name": "region", "required": true, "type": "string", "x-example": "EU"}, {"description": "Optional season number; when set the season-aware ranking is read.", "in": "query", "name": "season", "type": "integer", "x-example": 10}, {"description": "Optional page size, 1-100; default 20 and the gateway caps a page at 100 rows.", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/leaderboard", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "region", "required": true, "type": "string"}, {"in": "query", "name": "season", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-leaderboard-detail": {"bodyParam": null, "bodyRequired": false, "id": "faceit-leaderboard-detail", "method": "GET", "params": [{"description": "24-character leaderboard id from faceit-championship-search or faceit-standings.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "5b0d895ef2e59b000687c9ed"}], "path": "/faceit/leaderboard-detail", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-leaderboard-statuses": {"bodyParam": null, "bodyRequired": false, "id": "faceit-leaderboard-statuses", "method": "GET", "params": [], "path": "/faceit/leaderboard-statuses", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "faceit-maps": {"bodyParam": null, "bodyRequired": false, "id": "faceit-maps", "method": "GET", "params": [{"description": "Game slug, one of the values returned by faceit-games.", "enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}], "path": "/faceit/maps", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-match-clips": {"bodyParam": null, "bodyRequired": false, "id": "faceit-match-clips", "method": "GET", "params": [{"description": "Game slug; only cs2 has Allstar clips.", "enum": ["cs2"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2"}, {"description": "Upstream match id from a clip row, for example 1-bef84e57-4ce3-41aa-b5e5-2918228c1c28.", "in": "query", "name": "match_id", "required": true, "type": "string", "x-example": "1-bef84e57-4ce3-41aa-b5e5-2918228c1c28"}, {"description": "Optional page size, 1-100; default 10.", "in": "query", "name": "limit", "type": "integer", "x-example": 10}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/match-clips", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "match_id", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-organizer": {"bodyParam": null, "bodyRequired": false, "id": "faceit-organizer", "method": "GET", "params": [{"description": "Organizer UUID.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "73d4185d-559f-4dbc-8398-9eae47adfe27"}], "path": "/faceit/organizer", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-player": {"bodyParam": null, "bodyRequired": false, "id": "faceit-player", "method": "GET", "params": [{"description": "Optional FACEIT nickname; exactly one of nickname and user_id is required.", "in": "query", "name": "nickname", "type": "string", "x-example": "dem0nnnnnnnn"}, {"description": "Optional FACEIT user UUID; exactly one of nickname and user_id is required.", "in": "query", "name": "user_id", "type": "string", "x-example": "74df0e6b-5b41-42d7-93b4-05dc78b9a699"}], "path": "/faceit/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "nickname", "type": "string"}, {"in": "query", "name": "user_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-player-rank": {"bodyParam": null, "bodyRequired": false, "id": "faceit-player-rank", "method": "GET", "params": [{"description": "Game slug, one of the values returned by faceit-games.", "enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}, {"description": "Region code such as EU or NA; see faceit-regions for the documented values.", "in": "query", "name": "region", "required": true, "type": "string", "x-example": "EU"}, {"description": "Optional FACEIT nickname; exactly one of nickname and user_id is required.", "in": "query", "name": "nickname", "type": "string", "x-example": "dem0nnnnnnnn"}, {"description": "Optional FACEIT user UUID; exactly one of nickname and user_id is required.", "in": "query", "name": "user_id", "type": "string", "x-example": "74df0e6b-5b41-42d7-93b4-05dc78b9a699"}, {"description": "Optional season number; when set the season-aware ranking is read.", "in": "query", "name": "season", "type": "integer", "x-example": 10}], "path": "/faceit/player-rank", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "region", "required": true, "type": "string"}, {"in": "query", "name": "nickname", "type": "string"}, {"in": "query", "name": "user_id", "type": "string"}, {"in": "query", "name": "season", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-regions": {"bodyParam": null, "bodyRequired": false, "id": "faceit-regions", "method": "GET", "params": [], "path": "/faceit/regions", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "faceit-rule": {"bodyParam": null, "bodyRequired": false, "id": "faceit-rule", "method": "GET", "params": [{"description": "Rule UUID from faceit-rules.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "43e07c2c-c0b2-4872-9826-6812eba70463"}], "path": "/faceit/rule", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-rules": {"bodyParam": null, "bodyRequired": false, "id": "faceit-rules", "method": "GET", "params": [{"description": "Optional page size, 1-100; default 20.", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/rules", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-skill-levels": {"bodyParam": null, "bodyRequired": false, "id": "faceit-skill-levels", "method": "GET", "params": [{"description": "Game slug, one of the values returned by faceit-games.", "enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}], "path": "/faceit/skill-levels", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"], "in": "query", "name": "game", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-standings": {"bodyParam": null, "bodyRequired": false, "id": "faceit-standings", "method": "GET", "params": [{"description": "Championship UUID from faceit-championship-search.", "in": "query", "name": "entity_id", "required": true, "type": "string", "x-example": "9888a3f4-e292-4c3a-a511-15d5d2fb112b"}, {"description": "Group number.", "in": "query", "name": "group", "required": true, "type": "integer", "x-example": 1}, {"description": "Round number, or a comma-separated list such as 1,2.", "in": "query", "name": "round", "required": true, "type": "string", "x-example": "1"}, {"description": "Optional segment number; provide segment or match.", "in": "query", "name": "segment", "type": "integer", "x-example": 1}, {"description": "Optional match number; provide segment or match.", "in": "query", "name": "match", "type": "integer", "x-example": 1}], "path": "/faceit/standings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "entity_id", "required": true, "type": "string"}, {"in": "query", "name": "group", "required": true, "type": "integer"}, {"in": "query", "name": "round", "required": true, "type": "string"}, {"in": "query", "name": "segment", "type": "integer"}, {"in": "query", "name": "match", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-team": {"bodyParam": null, "bodyRequired": false, "id": "faceit-team", "method": "GET", "params": [{"description": "Team UUID from a premade bracket faction id.", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "3279bf46-2cd3-43d1-b4d7-2dfd24d1d843"}], "path": "/faceit/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "faceit-tournaments-past": {"bodyParam": null, "bodyRequired": false, "id": "faceit-tournaments-past", "method": "GET", "params": [{"description": "FACEIT nickname.", "in": "query", "name": "nickname", "required": true, "type": "string", "x-example": "dem0nnnnnnnn"}, {"description": "Optional page size, 1-100; default 20.", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Optional non-negative row offset.", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/faceit/tournaments-past", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "nickname", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "faceit-user-skills": {"bodyParam": null, "bodyRequired": false, "id": "faceit-user-skills", "method": "GET", "params": [{"collectionFormat": "multi", "description": "Required FACEIT user UUIDs; repeat the parameter for up to 10 users.", "in": "query", "items": {"type": "string"}, "name": "user_ids", "required": true, "type": "array", "x-example": "74df0e6b-5b41-42d7-93b4-05dc78b9a699"}, {"description": "Game slug, one of the values returned by faceit-games.", "in": "query", "name": "game", "required": true, "type": "string", "x-example": "cs2,csgo,ow2,valorant,pubg,tf2,krunker,pubgmobile,apex,fortnite,wow,brawl_stars,insidia,dota2,hearthstone,wildrift,clash_royale,smite,lol_NA,lol_EUW,lol_EUN,overwatch_EU,wot_EU,wot_RU,rainbow_6,csdz,battalion"}], "path": "/faceit/user-skills", "pathParams": [], "produces": ["application/json"], "queryParams": [{"collectionFormat": "multi", "in": "query", "name": "user_ids", "required": true, "type": "array"}, {"in": "query", "name": "game", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-faceit-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function ban_reasons(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-ban-reasons", $params, $responseType);
    }
    public function banlist(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-banlist", $params, $responseType);
    }
    public function banlist_stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-banlist-stats", $params, $responseType);
    }
    public function best_clips(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-best-clips", $params, $responseType);
    }
    public function championship(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-championship", $params, $responseType);
    }
    public function championship_bracket(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-championship-bracket", $params, $responseType);
    }
    public function championship_participants(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-championship-participants", $params, $responseType);
    }
    public function championship_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-championship-search", $params, $responseType);
    }
    public function clip(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-clip", $params, $responseType);
    }
    public function clips(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-clips", $params, $responseType);
    }
    public function competition_matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-competition-matches", $params, $responseType);
    }
    public function fpl(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-fpl", $params, $responseType);
    }
    public function game_modes(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-game-modes", $params, $responseType);
    }
    public function games(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-games", $params, $responseType);
    }
    public function hub(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-hub", $params, $responseType);
    }
    public function hub_categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-hub-categories", $params, $responseType);
    }
    public function hub_memberships(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-hub-memberships", $params, $responseType);
    }
    public function hubs(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-hubs", $params, $responseType);
    }
    public function hubs_detailed(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-hubs-detailed", $params, $responseType);
    }
    public function leaderboard(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-leaderboard", $params, $responseType);
    }
    public function leaderboard_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-leaderboard-detail", $params, $responseType);
    }
    public function leaderboard_statuses(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-leaderboard-statuses", $params, $responseType);
    }
    public function maps(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-maps", $params, $responseType);
    }
    public function match_clips(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-match-clips", $params, $responseType);
    }
    public function organizer(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-organizer", $params, $responseType);
    }
    public function player(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-player", $params, $responseType);
    }
    public function player_rank(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-player-rank", $params, $responseType);
    }
    public function regions(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-regions", $params, $responseType);
    }
    public function rule(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-rule", $params, $responseType);
    }
    public function rules(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-rules", $params, $responseType);
    }
    public function skill_levels(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-skill-levels", $params, $responseType);
    }
    public function standings(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-standings", $params, $responseType);
    }
    public function team(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-team", $params, $responseType);
    }
    public function tournaments_past(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-tournaments-past", $params, $responseType);
    }
    public function user_skills(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("faceit-user-skills", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
