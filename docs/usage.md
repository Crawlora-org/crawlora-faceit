# FACEIT API endpoint reference and client usage

This reference lists all 35 public FACEIT API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/faceit`, `crawlora-faceit`, and `crawlora-faceit` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape FACEIT locally; Crawlora is independent from and not endorsed by FACEIT or its owners.

The package tracks the public API contract revision `sha256:d14c7026f59aa4e03ae84775c08493086732dd9c06000fca9bb721c3772e03cb` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `faceit`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `banlist` | `banlist` | `faceit.banlist` | `GET /faceit/banlist` | `size` (query, optional), `cursor` (query, optional), `reason` (query, optional) | FACEIT public ban list page |
| `banlistStats` | `banlist_stats` | `faceit.banlist_stats` | `GET /faceit/banlist-stats` | — | FACEIT ban list aggregate counters |
| `banReasons` | `ban_reasons` | `faceit.ban_reasons` | `GET /faceit/ban-reasons` | — | FACEIT ban reason enum |
| `bestClips` | `best_clips` | `faceit.best_clips` | `GET /faceit/best-clips` | `game` (query, required; values: `cs2`), `user_id` (query, required), `from` (query, required), `to` (query, required), `limit` (query, optional) | FACEIT player best clips in a time window |
| `championship` | `championship` | `faceit.championship` | `GET /faceit/championship` | `id` (query, required) | FACEIT championship detail by id |
| `championshipBracket` | `championship_bracket` | `faceit.championship_bracket` | `GET /faceit/championship-bracket` | `id` (query, required), `group` (query, required), `round` (query, required), `start` (query, optional), `end` (query, optional) | FACEIT championship group bracket by group and round |
| `championshipParticipants` | `championship_participants` | `faceit.championship_participants` | `GET /faceit/championship-participants` | `id` (query, required), `limit` (query, optional), `offset` (query, optional) | FACEIT championship participants page |
| `championshipSearch` | `championship_search` | `faceit.championship_search` | `GET /faceit/championship-search` | `entity_type` (query, optional), `type` (query, optional), `status` (query, optional; values: `ONGOING`, `UPCOMING`, `FINISHED`), `subtype` (query, optional), `country` (query, optional), `game` (query, optional; values: `cs2`, `csgo`, `ow2`, `valorant`, `pubg`, `tf2`, `krunker`, `pubgmobile`, `apex`, `fortnite`, `wow`, `brawl_stars`, `insidia`, `dota2`, `hearthstone`, `wildrift`, `clash_royale`, `smite`, `lol_NA`, `lol_EUW`, `lol_EUN`, `overwatch_EU`, `wot_EU`, `wot_RU`, `rainbow_6`, `csdz`, `battalion`), `has_drops` (query, optional), `limit` (query, optional), `offset` (query, optional) | Discover FACEIT championships and leaderboards |
| `clip` | `clip` | `faceit.clip` | `GET /faceit/clip` | `id` (query, required) | FACEIT Allstar clip detail |
| `clips` | `clips` | `faceit.clips` | `GET /faceit/clips` | `game` (query, required; values: `cs2`), `user_id` (query, required), `limit` (query, optional), `offset` (query, optional) | FACEIT player Allstar clips |
| `competitionMatches` | `competition_matches` | `faceit.competition_matches` | `GET /faceit/competition-matches` | `id` (query, required), `type` (query, required), `player_id` (query, optional), `page` (query, optional), `size` (query, optional) | FACEIT competition match list |
| `fpl` | `fpl` | `faceit.fpl` | `GET /faceit/fpl` | `game` (query, optional; values: `cs2`, `csgo`, `ow2`, `valorant`, `pubg`, `tf2`, `krunker`, `pubgmobile`, `apex`, `fortnite`, `wow`, `brawl_stars`, `insidia`, `dota2`, `hearthstone`, `wildrift`, `clash_royale`, `smite`, `lol_NA`, `lol_EUW`, `lol_EUN`, `overwatch_EU`, `wot_EU`, `wot_RU`, `rainbow_6`, `csdz`, `battalion`), `limit` (query, optional), `offset` (query, optional) | FACEIT Pro League circuits |
| `gameModes` | `game_modes` | `faceit.game_modes` | `GET /faceit/game-modes` | `game` (query, required; values: `cs2`, `csgo`, `ow2`, `valorant`, `pubg`, `tf2`, `krunker`, `pubgmobile`, `apex`, `fortnite`, `wow`, `brawl_stars`, `insidia`, `dota2`, `hearthstone`, `wildrift`, `clash_royale`, `smite`, `lol_NA`, `lol_EUW`, `lol_EUN`, `overwatch_EU`, `wot_EU`, `wot_RU`, `rainbow_6`, `csdz`, `battalion`), `region` (query, required) | FACEIT public queues for a game and region |
| `games` | `games` | `faceit.games` | `GET /faceit/games` | — | FACEIT game slugs confirmed by the live map oracle |
| `hub` | `hub` | `faceit.hub` | `GET /faceit/hub` | `id` (query, required) | FACEIT hub detail by id |
| `hubCategories` | `hub_categories` | `faceit.hub_categories` | `GET /faceit/hub-categories` | — | FACEIT hub category enum |
| `hubMemberships` | `hub_memberships` | `faceit.hub_memberships` | `GET /faceit/hub-memberships` | `user_id` (query, required), `category` (query, optional; values: `community`, `chat`, `ihl`), `limit` (query, optional), `offset` (query, optional) | FACEIT user hub memberships |
| `hubs` | `hubs` | `faceit.hubs` | `GET /faceit/hubs` | `ids` (query, required) | FACEIT hubs by id |
| `hubsDetailed` | `hubs_detailed` | `faceit.hubs_detailed` | `GET /faceit/hubs-detailed` | `ids` (query, required) | FACEIT full hub objects for up to 20 ids |
| `leaderboard` | `leaderboard` | `faceit.leaderboard` | `GET /faceit/leaderboard` | `game` (query, required; values: `cs2`, `csgo`, `ow2`, `valorant`, `pubg`, `tf2`, `krunker`, `pubgmobile`, `apex`, `fortnite`, `wow`, `brawl_stars`, `insidia`, `dota2`, `hearthstone`, `wildrift`, `clash_royale`, `smite`, `lol_NA`, `lol_EUW`, `lol_EUN`, `overwatch_EU`, `wot_EU`, `wot_RU`, `rainbow_6`, `csdz`, `battalion`), `region` (query, required), `season` (query, optional), `limit` (query, optional), `offset` (query, optional) | FACEIT ranked leaderboard for one game and region |
| `leaderboardDetail` | `leaderboard_detail` | `faceit.leaderboard_detail` | `GET /faceit/leaderboard-detail` | `id` (query, required) | FACEIT leaderboard detail by id |
| `leaderboardStatuses` | `leaderboard_statuses` | `faceit.leaderboard_statuses` | `GET /faceit/leaderboard-statuses` | — | FACEIT leaderboard status enum |
| `maps` | `maps` | `faceit.maps` | `GET /faceit/maps` | `game` (query, required; values: `cs2`, `csgo`, `ow2`, `valorant`, `pubg`, `tf2`, `krunker`, `pubgmobile`, `apex`, `fortnite`, `wow`, `brawl_stars`, `insidia`, `dota2`, `hearthstone`, `wildrift`, `clash_royale`, `smite`, `lol_NA`, `lol_EUW`, `lol_EUN`, `overwatch_EU`, `wot_EU`, `wot_RU`, `rainbow_6`, `csdz`, `battalion`) | FACEIT votable maps for a game |
| `matchClips` | `match_clips` | `faceit.match_clips` | `GET /faceit/match-clips` | `game` (query, required; values: `cs2`), `match_id` (query, required), `limit` (query, optional), `offset` (query, optional) | FACEIT Allstar clips for one match |
| `organizer` | `organizer` | `faceit.organizer` | `GET /faceit/organizer` | `id` (query, required) | FACEIT organizer profile by id |
| `player` | `player` | `faceit.player` | `GET /faceit/player` | `nickname` (query, optional), `user_id` (query, optional) | FACEIT player profile by nickname or user id |
| `playerRank` | `player_rank` | `faceit.player_rank` | `GET /faceit/player-rank` | `game` (query, required; values: `cs2`, `csgo`, `ow2`, `valorant`, `pubg`, `tf2`, `krunker`, `pubgmobile`, `apex`, `fortnite`, `wow`, `brawl_stars`, `insidia`, `dota2`, `hearthstone`, `wildrift`, `clash_royale`, `smite`, `lol_NA`, `lol_EUW`, `lol_EUN`, `overwatch_EU`, `wot_EU`, `wot_RU`, `rainbow_6`, `csdz`, `battalion`), `region` (query, required), `nickname` (query, optional), `user_id` (query, optional), `season` (query, optional) | FACEIT player ranked position in one game and region |
| `regions` | `regions` | `faceit.regions` | `GET /faceit/regions` | — | FACEIT region codes known to the website |
| `rule` | `rule` | `faceit.rule` | `GET /faceit/rule` | `id` (query, required) | FACEIT competition rule detail |
| `rules` | `rules` | `faceit.rules` | `GET /faceit/rules` | `limit` (query, optional), `offset` (query, optional) | FACEIT published competition rules |
| `skillLevels` | `skill_levels` | `faceit.skill_levels` | `GET /faceit/skill-levels` | `game` (query, required; values: `cs2`, `csgo`, `ow2`, `valorant`, `pubg`, `tf2`, `krunker`, `pubgmobile`, `apex`, `fortnite`, `wow`, `brawl_stars`, `insidia`, `dota2`, `hearthstone`, `wildrift`, `clash_royale`, `smite`, `lol_NA`, `lol_EUW`, `lol_EUN`, `overwatch_EU`, `wot_EU`, `wot_RU`, `rainbow_6`, `csdz`, `battalion`) | FACEIT skill levels and Elo bands for a game |
| `standings` | `standings` | `faceit.standings` | `GET /faceit/standings` | `entity_id` (query, required), `group` (query, required), `round` (query, required), `segment` (query, optional), `match` (query, optional) | FACEIT championship standings by group and round |
| `team` | `team` | `faceit.team` | `GET /faceit/team` | `id` (query, required) | FACEIT team profile by id |
| `tournamentsPast` | `tournaments_past` | `faceit.tournaments_past` | `GET /faceit/tournaments-past` | `nickname` (query, required), `limit` (query, optional), `offset` (query, optional) | FACEIT player past tournament history |
| `userSkills` | `user_skills` | `faceit.user_skills` | `GET /faceit/user-skills` | `user_ids` (query, required), `game` (query, required) | FACEIT player skills for up to 10 users in one game |

## Client forms

- JavaScript: import `FaceitClient` (also exported as `Client`) from `@crawlora-org/faceit`; use `new FaceitClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `FaceitClient` (also exported as `Client`) from `crawlora_faceit`; use `with FaceitClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncFaceitClient`, used with `async with` and `await`.
- Rust: add `crawlora-faceit` with Cargo; import `Client` and the generated operation parameter struct, then call `client.faceit.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-faceit/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
