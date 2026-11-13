# FACEIT clients for Crawlora

Official Crawlora client packages for the hosted FACEIT API. Access 35 API endpoints covering leaderboards, players, teams, matches, tournaments, clips, hubs, and public game modes from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape FACEIT locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by FACEIT or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/faceit`](javascript/README.md)
- Python: [`crawlora-faceit`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-faceit`](go.mod)
- Ruby: [`crawlora-faceit`](ruby/README.md)
- Java: [`net.crawlora:crawlora-faceit:0.1.0`](java/README.md)
- PHP: [`crawlora/faceit`](php/README.md)
- Rust: [`crawlora-faceit`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=faceit-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=faceit-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=faceit-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 35 selected public FACEIT API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/faceit/ban-reasons` | `faceit-ban-reasons` | FACEIT ban reason enum |
| `GET` | `/faceit/banlist` | `faceit-banlist` | FACEIT public ban list page |
| `GET` | `/faceit/banlist-stats` | `faceit-banlist-stats` | FACEIT ban list aggregate counters |
| `GET` | `/faceit/best-clips` | `faceit-best-clips` | FACEIT player best clips in a time window |
| `GET` | `/faceit/championship` | `faceit-championship` | FACEIT championship detail by id |
| `GET` | `/faceit/championship-bracket` | `faceit-championship-bracket` | FACEIT championship group bracket by group and round |
| `GET` | `/faceit/championship-participants` | `faceit-championship-participants` | FACEIT championship participants page |
| `GET` | `/faceit/championship-search` | `faceit-championship-search` | Discover FACEIT championships and leaderboards |
| `GET` | `/faceit/clip` | `faceit-clip` | FACEIT Allstar clip detail |
| `GET` | `/faceit/clips` | `faceit-clips` | FACEIT player Allstar clips |
| `GET` | `/faceit/competition-matches` | `faceit-competition-matches` | FACEIT competition match list |
| `GET` | `/faceit/fpl` | `faceit-fpl` | FACEIT Pro League circuits |
| `GET` | `/faceit/game-modes` | `faceit-game-modes` | FACEIT public queues for a game and region |
| `GET` | `/faceit/games` | `faceit-games` | FACEIT game slugs confirmed by the live map oracle |
| `GET` | `/faceit/hub` | `faceit-hub` | FACEIT hub detail by id |
| `GET` | `/faceit/hub-categories` | `faceit-hub-categories` | FACEIT hub category enum |
| `GET` | `/faceit/hub-memberships` | `faceit-hub-memberships` | FACEIT user hub memberships |
| `GET` | `/faceit/hubs` | `faceit-hubs` | FACEIT hubs by id |
| `GET` | `/faceit/hubs-detailed` | `faceit-hubs-detailed` | FACEIT full hub objects for up to 20 ids |
| `GET` | `/faceit/leaderboard` | `faceit-leaderboard` | FACEIT ranked leaderboard for one game and region |
| `GET` | `/faceit/leaderboard-detail` | `faceit-leaderboard-detail` | FACEIT leaderboard detail by id |
| `GET` | `/faceit/leaderboard-statuses` | `faceit-leaderboard-statuses` | FACEIT leaderboard status enum |
| `GET` | `/faceit/maps` | `faceit-maps` | FACEIT votable maps for a game |
| `GET` | `/faceit/match-clips` | `faceit-match-clips` | FACEIT Allstar clips for one match |
| `GET` | `/faceit/organizer` | `faceit-organizer` | FACEIT organizer profile by id |
| `GET` | `/faceit/player` | `faceit-player` | FACEIT player profile by nickname or user id |
| `GET` | `/faceit/player-rank` | `faceit-player-rank` | FACEIT player ranked position in one game and region |
| `GET` | `/faceit/regions` | `faceit-regions` | FACEIT region codes known to the website |
| `GET` | `/faceit/rule` | `faceit-rule` | FACEIT competition rule detail |
| `GET` | `/faceit/rules` | `faceit-rules` | FACEIT published competition rules |
| `GET` | `/faceit/skill-levels` | `faceit-skill-levels` | FACEIT skill levels and Elo bands for a game |
| `GET` | `/faceit/standings` | `faceit-standings` | FACEIT championship standings by group and round |
| `GET` | `/faceit/team` | `faceit-team` | FACEIT team profile by id |
| `GET` | `/faceit/tournaments-past` | `faceit-tournaments-past` | FACEIT player past tournament history |
| `GET` | `/faceit/user-skills` | `faceit-user-skills` | FACEIT player skills for up to 10 users in one game |

## License

MIT. See [LICENSE](LICENSE).
