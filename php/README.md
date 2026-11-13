# Crawlora FACEIT API client for PHP (`crawlora/faceit`)

This PHP package calls Crawlora's hosted FACEIT API at `https://api.crawlora.net/api/v1`. It exposes 35 endpoints covering leaderboards, players, teams, matches, tournaments, clips, hubs, and public game modes. It does not call or scrape FACEIT directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/faceit
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=faceit-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=faceit-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Faceit\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("faceit-championship-search", []);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 35 API operations.

## Supported FACEIT API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-faceit/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=faceit-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=faceit-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-faceit). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-faceit/blob/main/docs/usage.md).
