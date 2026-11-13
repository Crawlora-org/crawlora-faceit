# crawlora-faceit — FACEIT API client for Python

Python client for Crawlora's hosted FACEIT API. It exposes 35 API endpoints covering leaderboards, players, teams, matches, tournaments, clips, hubs, and public game modes. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=faceit-python-homepage); the package does not run a browser or scrape
FACEIT locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
FACEIT or its owners.

## Install

```sh
python -m pip install crawlora-faceit
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=faceit-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=faceit-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_faceit import FaceitClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with FaceitClient(api_key=api_key) as client:
    result_1 = client.games()
    print(result_1)
    result_2 = client.banlist_stats()
    print(result_2)
```

The package also exports `Client` as an alias for `FaceitClient`. Operation
methods are available directly in snake_case and through the `faceit`
group. The async package client is `AsyncFaceitClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-faceit/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-faceit/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_faceit import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.games()
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-faceit/blob/main/examples/python.py) for a complete usage example.

## Supported FACEIT API endpoints

This package exposes every route below through direct snake_case methods and the `faceit` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-faceit/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
