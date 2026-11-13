# Crawlora FACEIT API client for Java

The official Java client for Crawlora's hosted FACEIT API. It exposes 35 endpoints covering leaderboards, players, teams, matches, tournaments, clips, hubs, and public game modes. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-faceit</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=faceit-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=faceit-java-console) to get an API key.

```java
import net.crawlora.faceit.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.games(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported FACEIT API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-faceit/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=faceit-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-faceit)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=faceit-java-api-docs)
