"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class FaceitClient(CrawloraClient):
    """Synchronous FACEIT API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-faceit-python/0.1.0')
        super().__init__(*args, **kwargs)

    def ban_reasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-ban-reasons', params, response_type=response_type, timeout=timeout, headers=headers)

    def banlist(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-banlist', params, response_type=response_type, timeout=timeout, headers=headers)

    def banlist_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-banlist-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def best_clips(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-best-clips', params, response_type=response_type, timeout=timeout, headers=headers)

    def championship(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-championship', params, response_type=response_type, timeout=timeout, headers=headers)

    def championship_bracket(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-championship-bracket', params, response_type=response_type, timeout=timeout, headers=headers)

    def championship_participants(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-championship-participants', params, response_type=response_type, timeout=timeout, headers=headers)

    def championship_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-championship-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def clip(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-clip', params, response_type=response_type, timeout=timeout, headers=headers)

    def clips(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-clips', params, response_type=response_type, timeout=timeout, headers=headers)

    def competition_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-competition-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def fpl(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-fpl', params, response_type=response_type, timeout=timeout, headers=headers)

    def game_modes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-game-modes', params, response_type=response_type, timeout=timeout, headers=headers)

    def games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-games', params, response_type=response_type, timeout=timeout, headers=headers)

    def hub(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-hub', params, response_type=response_type, timeout=timeout, headers=headers)

    def hub_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-hub-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def hub_memberships(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-hub-memberships', params, response_type=response_type, timeout=timeout, headers=headers)

    def hubs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-hubs', params, response_type=response_type, timeout=timeout, headers=headers)

    def hubs_detailed(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-hubs-detailed', params, response_type=response_type, timeout=timeout, headers=headers)

    def leaderboard(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-leaderboard', params, response_type=response_type, timeout=timeout, headers=headers)

    def leaderboard_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-leaderboard-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def leaderboard_statuses(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-leaderboard-statuses', params, response_type=response_type, timeout=timeout, headers=headers)

    def maps(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-maps', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_clips(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-match-clips', params, response_type=response_type, timeout=timeout, headers=headers)

    def organizer(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-organizer', params, response_type=response_type, timeout=timeout, headers=headers)

    def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-player', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_rank(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-player-rank', params, response_type=response_type, timeout=timeout, headers=headers)

    def regions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-regions', params, response_type=response_type, timeout=timeout, headers=headers)

    def rule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-rule', params, response_type=response_type, timeout=timeout, headers=headers)

    def rules(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-rules', params, response_type=response_type, timeout=timeout, headers=headers)

    def skill_levels(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-skill-levels', params, response_type=response_type, timeout=timeout, headers=headers)

    def standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    def team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-team', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournaments_past(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-tournaments-past', params, response_type=response_type, timeout=timeout, headers=headers)

    def user_skills(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('faceit-user-skills', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncFaceitClient(AsyncCrawloraClient):
    """Asynchronous FACEIT API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-faceit-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def ban_reasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-ban-reasons', params, response_type=response_type, timeout=timeout, headers=headers)

    async def banlist(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-banlist', params, response_type=response_type, timeout=timeout, headers=headers)

    async def banlist_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-banlist-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def best_clips(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-best-clips', params, response_type=response_type, timeout=timeout, headers=headers)

    async def championship(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-championship', params, response_type=response_type, timeout=timeout, headers=headers)

    async def championship_bracket(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-championship-bracket', params, response_type=response_type, timeout=timeout, headers=headers)

    async def championship_participants(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-championship-participants', params, response_type=response_type, timeout=timeout, headers=headers)

    async def championship_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-championship-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def clip(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-clip', params, response_type=response_type, timeout=timeout, headers=headers)

    async def clips(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-clips', params, response_type=response_type, timeout=timeout, headers=headers)

    async def competition_matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-competition-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def fpl(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-fpl', params, response_type=response_type, timeout=timeout, headers=headers)

    async def game_modes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-game-modes', params, response_type=response_type, timeout=timeout, headers=headers)

    async def games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-games', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hub(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-hub', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hub_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-hub-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hub_memberships(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-hub-memberships', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hubs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-hubs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def hubs_detailed(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-hubs-detailed', params, response_type=response_type, timeout=timeout, headers=headers)

    async def leaderboard(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-leaderboard', params, response_type=response_type, timeout=timeout, headers=headers)

    async def leaderboard_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-leaderboard-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def leaderboard_statuses(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-leaderboard-statuses', params, response_type=response_type, timeout=timeout, headers=headers)

    async def maps(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-maps', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_clips(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-match-clips', params, response_type=response_type, timeout=timeout, headers=headers)

    async def organizer(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-organizer', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-player', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_rank(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-player-rank', params, response_type=response_type, timeout=timeout, headers=headers)

    async def regions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-regions', params, response_type=response_type, timeout=timeout, headers=headers)

    async def rule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-rule', params, response_type=response_type, timeout=timeout, headers=headers)

    async def rules(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-rules', params, response_type=response_type, timeout=timeout, headers=headers)

    async def skill_levels(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-skill-levels', params, response_type=response_type, timeout=timeout, headers=headers)

    async def standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-team', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournaments_past(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-tournaments-past', params, response_type=response_type, timeout=timeout, headers=headers)

    async def user_skills(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('faceit-user-skills', params, response_type=response_type, timeout=timeout, headers=headers)
