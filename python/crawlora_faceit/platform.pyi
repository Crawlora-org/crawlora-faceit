from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelFaceitUserSkillsResponse = TypedDict('ModelFaceitUserSkillsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'skills': NotRequired[list[ModelFaceitUserSkill]],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitUserSkill = TypedDict('ModelFaceitUserSkill', {
    'expiration': NotRequired[str],
    'game_skill': NotRequired[ModelFaceitGameSkill],
    'is_professional_player': NotRequired[bool],
    'user_id': NotRequired[str],
}, total=False)

ModelFaceitGameSkill = TypedDict('ModelFaceitGameSkill', {
    'latest_delta': NotRequired[int],
    'level': NotRequired[int],
    'ranked_match_count': NotRequired[int],
    'value': NotRequired[int],
    'win_streak': NotRequired[int],
}, total=False)

ModelFaceitTournamentsPastResponse = TypedDict('ModelFaceitTournamentsPastResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'result': NotRequired[str],
    'size': NotRequired[int],
    'source_url': NotRequired[str],
    'tournaments': NotRequired[list[Any]],
}, total=False)

ModelFaceitTeamResponse = TypedDict('ModelFaceitTeamResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'team': NotRequired[ModelFaceitTeam],
}, total=False)

ModelFaceitTeam = TypedDict('ModelFaceitTeam', {
    'avatar': NotRequired[str],
    'country': NotRequired[str],
    'cover': NotRequired[str],
    'created_at': NotRequired[str],
    'description': NotRequired[str],
    'entity_type': NotRequired[str],
    'facebook': NotRequired[str],
    'game': NotRequired[str],
    'guid': NotRequired[str],
    'leader': NotRequired[str],
    'members': NotRequired[list[ModelFaceitTeamMember]],
    'members_ids': NotRequired[list[str]],
    'name': NotRequired[str],
    'nickname': NotRequired[str],
    'pending_members_ids': NotRequired[list[str]],
    'status': NotRequired[str],
    'team_type': NotRequired[str],
    'twitter': NotRequired[str],
    'updated_at': NotRequired[str],
    'website': NotRequired[str],
    'youtube': NotRequired[str],
}, total=False)

ModelFaceitTeamMember = TypedDict('ModelFaceitTeamMember', {
    'avatar': NotRequired[str],
    'country': NotRequired[str],
    'games': NotRequired[list[str]],
    'guid': NotRequired[str],
    'nickname': NotRequired[str],
}, total=False)

ModelFaceitStandingsResponse = TypedDict('ModelFaceitStandingsResponse', {
    'count': NotRequired[int],
    'entries': NotRequired[list[ModelFaceitStandingsEntry]],
    'fetched_at': NotRequired[str],
    'group': NotRequired[int],
    'round': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitStandingsEntry = TypedDict('ModelFaceitStandingsEntry', {
    'leaderboard': NotRequired[ModelFaceitStandingsLeaderboard],
    'rankings': NotRequired[list[ModelFaceitStandingsRanking]],
}, total=False)

ModelFaceitStandingsRanking = TypedDict('ModelFaceitStandingsRanking', {
    'placement': NotRequired[ModelFaceitStandingsPlacement],
    'played': NotRequired[int],
    'points': NotRequired[int],
    'position': NotRequired[int],
}, total=False)

ModelFaceitStandingsPlacement = TypedDict('ModelFaceitStandingsPlacement', {
    'entity_avatar': NotRequired[str],
    'entity_country': NotRequired[str],
    'entity_id': NotRequired[str],
    'entity_memberships': NotRequired[list[str]],
    'entity_name': NotRequired[str],
    'entity_skill_level': NotRequired[int],
    'entity_verified': NotRequired[bool],
    'entity_verified_level': NotRequired[str],
    'roster_ids': NotRequired[list[str]],
    'roster_memberships': NotRequired[list[str]],
    'type': NotRequired[str],
}, total=False)

ModelFaceitStandingsLeaderboard = TypedDict('ModelFaceitStandingsLeaderboard', {
    'bracket_placement': NotRequired[int],
    'delimiter': NotRequired[int],
    'entity_id': NotRequired[str],
    'entity_type': NotRequired[str],
    'group': NotRequired[int],
    'id': NotRequired[str],
    'round': NotRequired[int],
}, total=False)

ModelFaceitSkillLevelsResponse = TypedDict('ModelFaceitSkillLevelsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'levels': NotRequired[list[ModelFaceitSkillLevel]],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitSkillLevel = TypedDict('ModelFaceitSkillLevel', {
    'max': NotRequired[int],
    'min': NotRequired[int],
    'skill_level': NotRequired[int],
}, total=False)

ModelFaceitRulesResponse = TypedDict('ModelFaceitRulesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'rules': NotRequired[list[ModelFaceitRule]],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitRule = TypedDict('ModelFaceitRule', {
    'body': NotRequired[str],
    'created_at': NotRequired[str],
    'game': NotRequired[str],
    'guid': NotRequired[str],
    'name': NotRequired[str],
    'organizer': NotRequired[str],
    'updated_at': NotRequired[str],
}, total=False)

ModelFaceitRuleResponse = TypedDict('ModelFaceitRuleResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'rule': NotRequired[ModelFaceitRule],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitRegionsResponse = TypedDict('ModelFaceitRegionsResponse', {
    'closed': NotRequired[bool],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'regions': NotRequired[list[ModelFaceitRegion]],
    'source_url': NotRequired[str],
    'verified_at': NotRequired[str],
}, total=False)

ModelFaceitRegion = TypedDict('ModelFaceitRegion', {
    'code': NotRequired[str],
    'excluded': NotRequired[bool],
    'source': NotRequired[str],
}, total=False)

ModelFaceitPlayerRankResponse = TypedDict('ModelFaceitPlayerRankResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'position': NotRequired[int],
    'region': NotRequired[str],
    'season': NotRequired[int],
    'season_history': NotRequired[list[int]],
    'source_url': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

ModelFaceitPlayerResponse = TypedDict('ModelFaceitPlayerResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'player': NotRequired[ModelFaceitPlayer],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitPlayer = TypedDict('ModelFaceitPlayer', {
    'activated_at': NotRequired[str],
    'active_team_id': NotRequired[str],
    'avatar': NotRequired[str],
    'country': NotRequired[str],
    'cover_image_url': NotRequired[str],
    'created_at': NotRequired[str],
    'flag': NotRequired[str],
    'games': NotRequired[dict[str, ModelFaceitPlayerGame]],
    'id': NotRequired[str],
    'matching_sound': NotRequired[str],
    'memberships': NotRequired[list[str]],
    'nickname': NotRequired[str],
    'registration_status': NotRequired[str],
    'registration_status_v2': NotRequired[str],
    'tags': NotRequired[list[str]],
    'timezone': NotRequired[str],
    'user_type': NotRequired[str],
    'verified': NotRequired[bool],
}, total=False)

ModelFaceitPlayerGame = TypedDict('ModelFaceitPlayerGame', {
    'elo_refreshed_by_user_at': NotRequired[str],
    'faceit_elo': NotRequired[int],
    'game_id': NotRequired[str],
    'game_name': NotRequired[str],
    'region': NotRequired[str],
    'region_updated_at': NotRequired[str],
    'region_updated_at_v2': NotRequired[str],
    'skill_level': NotRequired[int],
    'skill_level_label': NotRequired[str],
    'tags': NotRequired[list[str]],
}, total=False)

ModelFaceitOrganizerResponse = TypedDict('ModelFaceitOrganizerResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'organizer': NotRequired[ModelFaceitOrganizer],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitOrganizer = TypedDict('ModelFaceitOrganizer', {
    'admin_list_public': NotRequired[bool],
    'admins': NotRequired[list[ModelFaceitOrganizerAdmin]],
    'avatar': NotRequired[str],
    'countries': NotRequired[list[str]],
    'cover': NotRequired[str],
    'description': NotRequired[str],
    'donations_enabled': NotRequired[bool],
    'facebook': NotRequired[str],
    'featured': NotRequired[bool],
    'features': NotRequired[list[str]],
    'featuring_countries': NotRequired[list[str]],
    'freemium_hub_enabled': NotRequired[bool],
    'games': NotRequired[list[str]],
    'geo_regions': NotRequired[list[str]],
    'guid': NotRequired[str],
    'live_streaming_enabled': NotRequired[bool],
    'name': NotRequired[str],
    'published': NotRequired[bool],
    'sponsors': NotRequired[list[ModelFaceitOrganizerSponsor]],
    'tier': NotRequired[ModelFaceitOrganizerTier],
    'twitch': NotRequired[str],
    'twitter': NotRequired[str],
    'type': NotRequired[str],
    'website': NotRequired[str],
}, total=False)

ModelFaceitOrganizerTier = TypedDict('ModelFaceitOrganizerTier', {
    'allowed_concurrent_competitions': NotRequired[int],
    'allowed_concurrent_hubs': NotRequired[int],
    'custom_prizes_enabled': NotRequired[bool],
    'faceit_points_prizes_enabled': NotRequired[bool],
    'level': NotRequired[int],
    'max_competition_slots': NotRequired[int],
    'max_rules': NotRequired[int],
    'min_competition_slots': NotRequired[int],
    'prize_money_settings_enabled': NotRequired[bool],
}, total=False)

ModelFaceitOrganizerSponsor = TypedDict('ModelFaceitOrganizerSponsor', {
    'guid': NotRequired[str],
    'image': NotRequired[str],
    'name': NotRequired[str],
    'priority': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelFaceitOrganizerAdmin = TypedDict('ModelFaceitOrganizerAdmin', {
    'avatar_url': NotRequired[str],
    'nickname': NotRequired[str],
    'role': NotRequired[str],
}, total=False)

ModelFaceitMatchClipsResponse = TypedDict('ModelFaceitMatchClipsResponse', {
    'clips': NotRequired[list[ModelFaceitClip]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitClip = TypedDict('ModelFaceitClip', {
    'created_at': NotRequired[str],
    'demo': NotRequired[str],
    'faceit_round': NotRequired[int],
    'id': NotRequired[str],
    'map': NotRequired[str],
    'match_id': NotRequired[str],
    'match_instance_id': NotRequired[str],
    'reason': NotRequired[str],
    'round': NotRequired[int],
    'status': NotRequired[str],
    'thumbnail_url': NotRequired[str],
    'title': NotRequired[str],
    'updated_at': NotRequired[str],
    'url': NotRequired[str],
    'user_id': NotRequired[str],
    'views': NotRequired[str],
}, total=False)

ModelFaceitMapsResponse = TypedDict('ModelFaceitMapsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'maps': NotRequired[list[ModelFaceitGameMap]],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitGameMap = TypedDict('ModelFaceitGameMap', {
    'class_name': NotRequired[str],
    'game_map_id': NotRequired[str],
    'guid': NotRequired[str],
    'image_lg': NotRequired[str],
    'image_sm': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFaceitLeaderboardStatusesResponse = TypedDict('ModelFaceitLeaderboardStatusesResponse', {
    'count': NotRequired[int],
    'entity_types': NotRequired[list[str]],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'statuses': NotRequired[list[str]],
    'types': NotRequired[list[str]],
    'verified_at': NotRequired[str],
}, total=False)

ModelFaceitLeaderboardDetailResponse = TypedDict('ModelFaceitLeaderboardDetailResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'leaderboard': NotRequired[ModelFaceitLeaderboardDetail],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitLeaderboardDetail = TypedDict('ModelFaceitLeaderboardDetail', {
    'balanced_scoring': NotRequired[Any],
    'bracket_placement': NotRequired[int],
    'bye_team_result_action': NotRequired[str],
    'conclusion_criteria': NotRequired[str],
    'country_restriction': NotRequired[str],
    'created_at': NotRequired[str],
    'delimiter': NotRequired[int],
    'drops_information': NotRequired[Any],
    'end_date': NotRequired[str],
    'entities': NotRequired[list[ModelFaceitLeaderboardEntityRef]],
    'entity_id': NotRequired[str],
    'entity_type': NotRequired[str],
    'ffa_points': NotRequired[dict[str, int]],
    'game': NotRequired[str],
    'group': NotRequired[int],
    'hidden': NotRequired[bool],
    'id': NotRequired[str],
    'last_modified': NotRequired[str],
    'leaderboard_mode': NotRequired[str],
    'leaderboard_name': NotRequired[str],
    'leaderboard_type': NotRequired[str],
    'membership_requirement': NotRequired[Any],
    'metadata': NotRequired[Any],
    'min_matches': NotRequired[int],
    'notify_points_updates': NotRequired[bool],
    'organizer_id': NotRequired[str],
    'penalty': NotRequired[Any],
    'points_per': NotRequired[Any],
    'points_per_draw': NotRequired[int],
    'points_per_loss': NotRequired[int],
    'points_per_win': NotRequired[int],
    'points_type': NotRequired[str],
    'prize_pool': NotRequired[Any],
    'prizes': NotRequired[Any],
    'promotion_target': NotRequired[Any],
    'ranking_boost': NotRequired[int],
    'ranking_fields': NotRequired[Any],
    'ranking_type': NotRequired[str],
    'region': NotRequired[str],
    'relegation_target': NotRequired[Any],
    'requirement': NotRequired[Any],
    'round': NotRequired[int],
    'rules': NotRequired[Any],
    'schedule': NotRequired[str],
    'season': NotRequired[int],
    'start_date': NotRequired[str],
    'starting_points': NotRequired[int],
    'status': NotRequired[str],
    'subtype': NotRequired[Any],
    'tag_requirement': NotRequired[Any],
    'technical_name': NotRequired[str],
    'version': NotRequired[int],
}, total=False)

ModelFaceitLeaderboardEntityRef = TypedDict('ModelFaceitLeaderboardEntityRef', {
    'id': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFaceitLeaderboardResponse = TypedDict('ModelFaceitLeaderboardResponse', {
    'count': NotRequired[int],
    'entries': NotRequired[list[ModelFaceitRankingEntry]],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'region': NotRequired[str],
    'season': NotRequired[int],
    'season_history': NotRequired[list[int]],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitRankingEntry = TypedDict('ModelFaceitRankingEntry', {
    'elo': NotRequired[int],
    'global_position': NotRequired[int],
    'position': NotRequired[int],
    'skill_level': NotRequired[int],
    'user': NotRequired[ModelFaceitRankingUser],
    'verification_level': NotRequired[int],
}, total=False)

ModelFaceitRankingUser = TypedDict('ModelFaceitRankingUser', {
    'country': NotRequired[str],
    'id': NotRequired[str],
    'nickname': NotRequired[str],
}, total=False)

ModelFaceitHubsDetailedResponse = TypedDict('ModelFaceitHubsDetailedResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'items': NotRequired[list[ModelFaceitHubDetailed]],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitHubDetailed = TypedDict('ModelFaceitHubDetailed', {
    'admin_tool_enabled': NotRequired[bool],
    'application_configuration': NotRequired[ModelFaceitHubApplicationSettings],
    'archived': NotRequired[bool],
    'avatar': NotRequired[str],
    'category': NotRequired[str],
    'chat_settings': NotRequired[ModelFaceitHubChatSettings],
    'check_game': NotRequired[bool],
    'check_geo_location': NotRequired[bool],
    'check_region': NotRequired[bool],
    'child_ids': NotRequired[list[str]],
    'clash_slots_available': NotRequired[bool],
    'club': NotRequired[bool],
    'cover_image': NotRequired[str],
    'created_at': NotRequired[str],
    'current_players_joined': NotRequired[int],
    'custom_prizes_count': NotRequired[int],
    'description': NotRequired[str],
    'faceit_points_equivalent_total': NotRequired[int],
    'faceit_points_total': NotRequired[int],
    'featured': NotRequired[bool],
    'game': NotRequired[str],
    'guid': NotRequired[str],
    'join_permissions': NotRequired[str],
    'max_skill_level': NotRequired[int],
    'min_skill_level': NotRequired[int],
    'name': NotRequired[str],
    'organizer_guid': NotRequired[str],
    'owner': NotRequired[ModelFaceitHubOwner],
    'published': NotRequired[bool],
    'region': NotRequired[str],
    'relationship_type': NotRequired[str],
    'roles': NotRequired[list[ModelFaceitHubRole]],
    'rules_guid': NotRequired[str],
    'selection_settings': NotRequired[ModelFaceitHubSelectionSettings],
    'sensitive': NotRequired[bool],
    'slots': NotRequired[int],
    'supporter_badge_image': NotRequired[str],
}, total=False)

ModelFaceitHubSelectionSettings = TypedDict('ModelFaceitHubSelectionSettings', {
    'enabled': NotRequired[bool],
}, total=False)

ModelFaceitHubRole = TypedDict('ModelFaceitHubRole', {
    'color': NotRequired[str],
    'guid': NotRequired[str],
    'name': NotRequired[str],
    'ranking': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelFaceitHubOwner = TypedDict('ModelFaceitHubOwner', {
    'avatar_url': NotRequired[str],
    'guid': NotRequired[str],
    'nickname': NotRequired[str],
}, total=False)

ModelFaceitHubChatSettings = TypedDict('ModelFaceitHubChatSettings', {
    'join_announcements': NotRequired[bool],
    'subscription_announcements': NotRequired[str],
}, total=False)

ModelFaceitHubApplicationSettings = TypedDict('ModelFaceitHubApplicationSettings', {
    'applicant_input_required': NotRequired[bool],
    'applications_enabled': NotRequired[bool],
}, total=False)

ModelFaceitHubsResponse = TypedDict('ModelFaceitHubsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'items': NotRequired[list[ModelFaceitHubSummary]],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitHubSummary = TypedDict('ModelFaceitHubSummary', {
    'avatar': NotRequired[str],
    'category': NotRequired[str],
    'child_ids': NotRequired[list[str]],
    'club': NotRequired[bool],
    'current_players_joined': NotRequired[int],
    'game': NotRequired[str],
    'guid': NotRequired[str],
    'name': NotRequired[str],
    'organizer_guid': NotRequired[str],
    'organizer_tier': NotRequired[int],
    'published': NotRequired[bool],
    'region': NotRequired[str],
    'relationship_type': NotRequired[str],
}, total=False)

ModelFaceitHubMembershipsResponse = TypedDict('ModelFaceitHubMembershipsResponse', {
    'count': NotRequired[int],
    'end': NotRequired[int],
    'fetched_at': NotRequired[str],
    'items': NotRequired[list[ModelFaceitHubMembership]],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'source_url': NotRequired[str],
    'start': NotRequired[int],
}, total=False)

ModelFaceitHubMembership = TypedDict('ModelFaceitHubMembership', {
    'competition': NotRequired[ModelFaceitHubCompetition],
    'created_at': NotRequired[str],
    'highest_role_ranking': NotRequired[int],
    'membership_id': NotRequired[str],
    'roles': NotRequired[list[str]],
    'user': NotRequired[ModelFaceitHubMemberUser],
}, total=False)

ModelFaceitHubMemberUser = TypedDict('ModelFaceitHubMemberUser', {
    'avatar_url': NotRequired[str],
    'guid': NotRequired[str],
    'nickname': NotRequired[str],
}, total=False)

ModelFaceitHubCompetition = TypedDict('ModelFaceitHubCompetition', {
    'announcement': NotRequired[str],
    'avatar': NotRequired[str],
    'category': NotRequired[str],
    'child_ids': NotRequired[list[str]],
    'current_players_joined': NotRequired[int],
    'custom_prizes_count': NotRequired[int],
    'game': NotRequired[str],
    'guid': NotRequired[str],
    'join_permissions': NotRequired[str],
    'max_skill_level': NotRequired[int],
    'min_skill_level': NotRequired[int],
    'name': NotRequired[str],
    'organizer_name': NotRequired[str],
    'published': NotRequired[bool],
    'whitelist_geo_countries': NotRequired[list[str]],
}, total=False)

ModelFaceitHubCategoriesResponse = TypedDict('ModelFaceitHubCategoriesResponse', {
    'categories': NotRequired[list[str]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'verified_at': NotRequired[str],
}, total=False)

ModelFaceitHubResponse = TypedDict('ModelFaceitHubResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'hub': NotRequired[ModelFaceitHub],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitHub = TypedDict('ModelFaceitHub', {
    'admin_tool_enabled': NotRequired[bool],
    'application_configuration': NotRequired[ModelFaceitHubApplicationSettings],
    'archived': NotRequired[bool],
    'avatar': NotRequired[str],
    'category': NotRequired[str],
    'chat_settings': NotRequired[ModelFaceitHubChatSettings],
    'check_game': NotRequired[bool],
    'check_geo_location': NotRequired[bool],
    'check_region': NotRequired[bool],
    'child_ids': NotRequired[list[str]],
    'children': NotRequired[list[ModelFaceitHubChild]],
    'clash_slots_available': NotRequired[bool],
    'club': NotRequired[bool],
    'cover_image': NotRequired[str],
    'created_at': NotRequired[str],
    'current_players_joined': NotRequired[int],
    'custom_prizes_count': NotRequired[int],
    'description': NotRequired[str],
    'faceit_points_equivalent_total': NotRequired[int],
    'faceit_points_total': NotRequired[int],
    'featured': NotRequired[bool],
    'game': NotRequired[str],
    'guid': NotRequired[str],
    'join_permissions': NotRequired[str],
    'max_skill_level': NotRequired[int],
    'min_skill_level': NotRequired[int],
    'name': NotRequired[str],
    'organizer_guid': NotRequired[str],
    'organizer_name': NotRequired[str],
    'published': NotRequired[bool],
    'region': NotRequired[str],
    'relationship_type': NotRequired[str],
    'roles': NotRequired[list[ModelFaceitHubRole]],
    'rules_guid': NotRequired[str],
    'selection_settings': NotRequired[ModelFaceitHubSelectionSettings],
    'sensitive': NotRequired[bool],
    'slots': NotRequired[int],
    'supporter_badge_image': NotRequired[str],
}, total=False)

ModelFaceitHubChild = TypedDict('ModelFaceitHubChild', {
    'category': NotRequired[str],
    'current_players_joined': NotRequired[int],
    'game': NotRequired[str],
    'guid': NotRequired[str],
    'name': NotRequired[str],
    'parent_id': NotRequired[str],
    'published': NotRequired[bool],
    'region': NotRequired[str],
    'relationship_type': NotRequired[str],
}, total=False)

ModelFaceitGamesResponse = TypedDict('ModelFaceitGamesResponse', {
    'complete': NotRequired[bool],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'games': NotRequired[list[ModelFaceitGame]],
    'source_url': NotRequired[str],
    'verified_at': NotRequired[str],
}, total=False)

ModelFaceitGame = TypedDict('ModelFaceitGame', {
    'clips': NotRequired[bool],
    'leaderboard_verified': NotRequired[bool],
    'map_configuration': NotRequired[bool],
    'slug': NotRequired[str],
}, total=False)

ModelFaceitGameModesResponse = TypedDict('ModelFaceitGameModesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'modes': NotRequired[list[ModelFaceitGameMode]],
    'region': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitGameMode = TypedDict('ModelFaceitGameMode', {
    'group_id': NotRequired[str],
    'id': NotRequired[str],
    'label': NotRequired[dict[str, str]],
    'spectators': NotRequired[bool],
    'team_size': NotRequired[int],
}, total=False)

ModelFaceitFplresponse = TypedDict('ModelFaceitFplresponse', {
    'circuits': NotRequired[list[ModelFaceitFplcircuit]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitFplcircuit = TypedDict('ModelFaceitFplcircuit', {
    'default': NotRequired[bool],
    'game': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'ranking_source': NotRequired[ModelFaceitFplrankingSource],
    'region': NotRequired[str],
    'seasons': NotRequired[list[ModelFaceitFplseason]],
}, total=False)

ModelFaceitFplseason = TypedDict('ModelFaceitFplseason', {
    'ended_at': NotRequired[str],
    'number': NotRequired[int],
    'started_at': NotRequired[str],
}, total=False)

ModelFaceitFplrankingSource = TypedDict('ModelFaceitFplrankingSource', {
    'source': NotRequired[str],
}, total=False)

ModelFaceitCompetitionMatchesResponse = TypedDict('ModelFaceitCompetitionMatchesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'matches': NotRequired[list[Any]],
    'page': NotRequired[int],
    'size': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitClipsResponse = TypedDict('ModelFaceitClipsResponse', {
    'clips': NotRequired[list[ModelFaceitClip]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitClipResponse = TypedDict('ModelFaceitClipResponse', {
    'clip': NotRequired[ModelFaceitClip],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitChampionshipSearchResponse = TypedDict('ModelFaceitChampionshipSearchResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'items': NotRequired[list[ModelFaceitLeaderboard]],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitLeaderboard = TypedDict('ModelFaceitLeaderboard', {
    'bracket_placement': NotRequired[int],
    'bye_team_result_action': NotRequired[str],
    'conclusion_criteria': NotRequired[str],
    'country_restriction': NotRequired[str],
    'delimiter': NotRequired[int],
    'drops_information': NotRequired[Any],
    'end_date': NotRequired[str],
    'entity_id': NotRequired[str],
    'entity_type': NotRequired[str],
    'ffa_points': NotRequired[dict[str, int]],
    'game': NotRequired[str],
    'group': NotRequired[int],
    'hidden': NotRequired[bool],
    'id': NotRequired[str],
    'leaderboard_mode': NotRequired[str],
    'leaderboard_name': NotRequired[str],
    'leaderboard_type': NotRequired[str],
    'min_matches': NotRequired[int],
    'organizer_id': NotRequired[str],
    'points_per_draw': NotRequired[int],
    'points_per_loss': NotRequired[int],
    'points_per_win': NotRequired[int],
    'points_type': NotRequired[str],
    'prize_pool': NotRequired[Any],
    'prizes': NotRequired[Any],
    'ranking_type': NotRequired[str],
    'region': NotRequired[str],
    'round': NotRequired[int],
    'rules': NotRequired[Any],
    'schedule': NotRequired[str],
    'season': NotRequired[int],
    'start_date': NotRequired[str],
    'starting_points': NotRequired[int],
    'status': NotRequired[str],
    'technical_name': NotRequired[str],
}, total=False)

ModelFaceitChampionshipParticipantsResponse = TypedDict('ModelFaceitChampionshipParticipantsResponse', {
    'count': NotRequired[int],
    'end': NotRequired[int],
    'fetched_at': NotRequired[str],
    'items': NotRequired[list[ModelFaceitChampionshipMember]],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'source_url': NotRequired[str],
    'start': NotRequired[int],
}, total=False)

ModelFaceitChampionshipMember = TypedDict('ModelFaceitChampionshipMember', {
    'championship': NotRequired[ModelFaceitChampionshipMemberEvent],
    'championship_status': NotRequired[str],
    'id': NotRequired[str],
    'roles': NotRequired[list[str]],
    'user': NotRequired[ModelFaceitChampionshipMemberUser],
}, total=False)

ModelFaceitChampionshipMemberUser = TypedDict('ModelFaceitChampionshipMemberUser', {
    'avatar_url': NotRequired[str],
    'country': NotRequired[str],
    'games': NotRequired[list[str]],
    'id': NotRequired[str],
    'nickname': NotRequired[str],
}, total=False)

ModelFaceitChampionshipMemberEvent = TypedDict('ModelFaceitChampionshipMemberEvent', {
    'game': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'organizer_id': NotRequired[str],
}, total=False)

ModelFaceitChampionshipBracketResponse = TypedDict('ModelFaceitChampionshipBracketResponse', {
    'count': NotRequired[int],
    'end': NotRequired[int],
    'fetched_at': NotRequired[str],
    'items': NotRequired[list[ModelFaceitChampionshipBracketGroup]],
    'source_url': NotRequired[str],
    'start': NotRequired[int],
    'total': NotRequired[int],
}, total=False)

ModelFaceitChampionshipBracketGroup = TypedDict('ModelFaceitChampionshipBracketGroup', {
    'championship_id': NotRequired[str],
    'delimiter': NotRequired[int],
    'group': NotRequired[int],
    'matches': NotRequired[list[ModelFaceitChampionshipBracketMatch]],
    'number': NotRequired[int],
    'status': NotRequired[str],
}, total=False)

ModelFaceitChampionshipBracketMatch = TypedDict('ModelFaceitChampionshipBracketMatch', {
    'bracket_placement': NotRequired[int],
    'factions': NotRequired[list[ModelFaceitChampionshipFaction]],
    'status': NotRequired[str],
    'total_factions': NotRequired[int],
}, total=False)

ModelFaceitChampionshipFaction = TypedDict('ModelFaceitChampionshipFaction', {
    'id': NotRequired[str],
    'number': NotRequired[int],
}, total=False)

ModelFaceitChampionshipResponse = TypedDict('ModelFaceitChampionshipResponse', {
    'championship': NotRequired[ModelFaceitChampionship],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitChampionship = TypedDict('ModelFaceitChampionship', {
    'ac_required': NotRequired[bool],
    'admin_tool_enabled': NotRequired[bool],
    'archived': NotRequired[bool],
    'calculate_elo': NotRequired[bool],
    'championship_start': NotRequired[int],
    'checkin_clear': NotRequired[int],
    'checkin_enabled': NotRequired[bool],
    'checkin_start': NotRequired[int],
    'current_subscriptions': NotRequired[int],
    'featured': NotRequired[bool],
    'full': NotRequired[bool],
    'game': NotRequired[str],
    'group_seeding_strategy': NotRequired[str],
    'groups': NotRequired[dict[str, ModelFaceitChampionshipGroup]],
    'id': NotRequired[str],
    'join_checks': NotRequired[ModelFaceitChampionshipJoinChecks],
    'leaderboard_points': NotRequired[dict[str, int]],
    'match_configuration': NotRequired[ModelFaceitChampionshipMatchConfiguration],
    'name': NotRequired[str],
    'organizer': NotRequired[ModelFaceitChampionshipOrganizer],
    'organizer_id': NotRequired[str],
    'participants': NotRequired[ModelFaceitChampionshipParticipants],
    'published': NotRequired[bool],
    'ranking_type': NotRequired[str],
    'region': NotRequired[str],
    'roles': NotRequired[list[ModelFaceitChampionshipRole]],
    'round_seeding_strategy': NotRequired[str],
    'schedule': NotRequired[dict[str, ModelFaceitChampionshipSchedule]],
    'slots': NotRequired[int],
    'status': NotRequired[str],
    'subscription_end': NotRequired[int],
    'subscription_start': NotRequired[int],
    'subscriptions_locked': NotRequired[bool],
    'substitution': NotRequired[ModelFaceitChampionshipSubstitution],
    'total_groups': NotRequired[int],
    'total_rounds': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelFaceitChampionshipSubstitution = TypedDict('ModelFaceitChampionshipSubstitution', {
    'max_substitutes': NotRequired[int],
    'max_substitutions': NotRequired[int],
    'substitution_time': NotRequired[int],
    'substitutions_per_round_enabled': NotRequired[bool],
}, total=False)

ModelFaceitChampionshipSchedule = TypedDict('ModelFaceitChampionshipSchedule', {
    'date': NotRequired[int],
    'status': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFaceitChampionshipRole = TypedDict('ModelFaceitChampionshipRole', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFaceitChampionshipParticipants = TypedDict('ModelFaceitChampionshipParticipants', {
    'total': NotRequired[int],
    'with_reserved_slot': NotRequired[int],
}, total=False)

ModelFaceitChampionshipOrganizer = TypedDict('ModelFaceitChampionshipOrganizer', {
    'features': NotRequired[list[str]],
    'name': NotRequired[str],
}, total=False)

ModelFaceitChampionshipMatchConfiguration = TypedDict('ModelFaceitChampionshipMatchConfiguration', {
    'best_of': NotRequired[int],
    'elo_type': NotRequired[str],
    'game': NotRequired[str],
    'game_type': NotRequired[str],
    'id': NotRequired[str],
    'label_en': NotRequired[str],
    'max_players': NotRequired[int],
    'name': NotRequired[str],
    'region': NotRequired[str],
    'team_size': NotRequired[int],
}, total=False)

ModelFaceitChampionshipJoinChecks = TypedDict('ModelFaceitChampionshipJoinChecks', {
    'allowed_team_types': NotRequired[list[str]],
    'blacklist_geo_countries': NotRequired[list[str]],
    'join_policy': NotRequired[str],
    'max_skill_level': NotRequired[int],
    'min_skill_level': NotRequired[int],
    'whitelist_geo_countries': NotRequired[list[str]],
}, total=False)

ModelFaceitChampionshipGroup = TypedDict('ModelFaceitChampionshipGroup', {
    'capacity': NotRequired[int],
}, total=False)

ModelFaceitBestClipsResponse = TypedDict('ModelFaceitBestClipsResponse', {
    'clips': NotRequired[list[ModelFaceitClip]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'from': NotRequired[str],
    'game': NotRequired[str],
    'limit': NotRequired[int],
    'source_url': NotRequired[str],
    'to': NotRequired[str],
}, total=False)

ModelFaceitBanlistStatsResponse = TypedDict('ModelFaceitBanlistStatsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'last_12_months': NotRequired[int],
    'last_30_days': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitBanlistResponse = TypedDict('ModelFaceitBanlistResponse', {
    'bans': NotRequired[list[ModelFaceitBan]],
    'count': NotRequired[int],
    'cursor': NotRequired[str],
    'fetched_at': NotRequired[str],
    'size': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelFaceitBan = TypedDict('ModelFaceitBan', {
    'avatar': NotRequired[str],
    'country': NotRequired[str],
    'duration_in_millis': NotRequired[int],
    'ends_at': NotRequired[str],
    'id': NotRequired[str],
    'nickname': NotRequired[str],
    'reason': NotRequired[str],
    'starts_at': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

ModelFaceitBanReasonsResponse = TypedDict('ModelFaceitBanReasonsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'reasons': NotRequired[list[str]],
    'source_url': NotRequired[str],
    'verified_at': NotRequired[str],
}, total=False)

FaceitBanReasonsResponse = Any
FaceitBanReasonsParams = TypedDict('FaceitBanReasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FaceitBanlistResponse = Any
FaceitBanlistParams = TypedDict('FaceitBanlistParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'size': NotRequired[int],
    'cursor': NotRequired[str],
    'reason': NotRequired[str],
}, total=False)

FaceitBanlistStatsResponse = Any
FaceitBanlistStatsParams = TypedDict('FaceitBanlistStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FaceitBestClipsResponse = Any
FaceitBestClipsParams = TypedDict('FaceitBestClipsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['cs2']],
    'user_id': Required[str],
    'from': Required[str],
    'to': Required[str],
    'limit': NotRequired[int],
}, total=False)

FaceitChampionshipResponse = Any
FaceitChampionshipParams = TypedDict('FaceitChampionshipParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FaceitChampionshipBracketResponse = Any
FaceitChampionshipBracketParams = TypedDict('FaceitChampionshipBracketParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'group': Required[int],
    'round': Required[int],
    'start': NotRequired[int],
    'end': NotRequired[int],
}, total=False)

FaceitChampionshipParticipantsResponse = Any
FaceitChampionshipParticipantsParams = TypedDict('FaceitChampionshipParticipantsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitChampionshipSearchResponse = Any
FaceitChampionshipSearchParams = TypedDict('FaceitChampionshipSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'entity_type': NotRequired[str],
    'type': NotRequired[str],
    'status': NotRequired[Literal['ONGOING', 'UPCOMING', 'FINISHED']],
    'subtype': NotRequired[str],
    'country': NotRequired[str],
    'game': NotRequired[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'has_drops': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitClipResponse = Any
FaceitClipParams = TypedDict('FaceitClipParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FaceitClipsResponse = Any
FaceitClipsParams = TypedDict('FaceitClipsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['cs2']],
    'user_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitCompetitionMatchesResponse = Any
FaceitCompetitionMatchesParams = TypedDict('FaceitCompetitionMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'type': Required[str],
    'player_id': NotRequired[str],
    'page': NotRequired[int],
    'size': NotRequired[int],
}, total=False)

FaceitFplResponse = Any
FaceitFplParams = TypedDict('FaceitFplParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitGameModesResponse = Any
FaceitGameModesParams = TypedDict('FaceitGameModesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'region': Required[str],
}, total=False)

FaceitGamesResponse = Any
FaceitGamesParams = TypedDict('FaceitGamesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FaceitHubResponse = Any
FaceitHubParams = TypedDict('FaceitHubParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FaceitHubCategoriesResponse = Any
FaceitHubCategoriesParams = TypedDict('FaceitHubCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FaceitHubMembershipsResponse = Any
FaceitHubMembershipsParams = TypedDict('FaceitHubMembershipsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': Required[str],
    'category': NotRequired[Literal['community', 'chat', 'ihl']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitHubsResponse = Any
FaceitHubsParams = TypedDict('FaceitHubsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ids': Required[list[str]],
}, total=False)

FaceitHubsDetailedResponse = Any
FaceitHubsDetailedParams = TypedDict('FaceitHubsDetailedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ids': Required[list[str]],
}, total=False)

FaceitLeaderboardResponse = Any
FaceitLeaderboardParams = TypedDict('FaceitLeaderboardParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'region': Required[str],
    'season': NotRequired[int],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitLeaderboardDetailResponse = Any
FaceitLeaderboardDetailParams = TypedDict('FaceitLeaderboardDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FaceitLeaderboardStatusesResponse = Any
FaceitLeaderboardStatusesParams = TypedDict('FaceitLeaderboardStatusesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FaceitMapsResponse = Any
FaceitMapsParams = TypedDict('FaceitMapsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
}, total=False)

FaceitMatchClipsResponse = Any
FaceitMatchClipsParams = TypedDict('FaceitMatchClipsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['cs2']],
    'match_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitOrganizerResponse = Any
FaceitOrganizerParams = TypedDict('FaceitOrganizerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FaceitPlayerResponse = Any
FaceitPlayerParams = TypedDict('FaceitPlayerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'nickname': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

FaceitPlayerRankResponse = Any
FaceitPlayerRankParams = TypedDict('FaceitPlayerRankParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'region': Required[str],
    'nickname': NotRequired[str],
    'user_id': NotRequired[str],
    'season': NotRequired[int],
}, total=False)

FaceitRegionsResponse = Any
FaceitRegionsParams = TypedDict('FaceitRegionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FaceitRuleResponse = Any
FaceitRuleParams = TypedDict('FaceitRuleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FaceitRulesResponse = Any
FaceitRulesParams = TypedDict('FaceitRulesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitSkillLevelsResponse = Any
FaceitSkillLevelsParams = TypedDict('FaceitSkillLevelsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
}, total=False)

FaceitStandingsResponse = Any
FaceitStandingsParams = TypedDict('FaceitStandingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'entity_id': Required[str],
    'group': Required[int],
    'round': Required[str],
    'segment': NotRequired[int],
    'match': NotRequired[int],
}, total=False)

FaceitTeamResponse = Any
FaceitTeamParams = TypedDict('FaceitTeamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FaceitTournamentsPastResponse = Any
FaceitTournamentsPastParams = TypedDict('FaceitTournamentsPastParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'nickname': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitUserSkillsResponse = Any
FaceitUserSkillsParams = TypedDict('FaceitUserSkillsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_ids': Required[list[str]],
    'game': Required[str],
}, total=False)

class FaceitGroup:
    @overload
    def ban_reasons(self, **params: Unpack[FaceitBanReasonsStreamParams]) -> BinaryIO: ...
    @overload
    def ban_reasons(self, **params: Unpack[FaceitBanReasonsTextResponseParams]) -> str: ...
    @overload
    def ban_reasons(self, **params: Unpack[FaceitBanReasonsDefaultParams]) -> FaceitBanReasonsResponse: ...
    @overload
    def banlist(self, **params: Unpack[FaceitBanlistStreamParams]) -> BinaryIO: ...
    @overload
    def banlist(self, **params: Unpack[FaceitBanlistTextResponseParams]) -> str: ...
    @overload
    def banlist(self, **params: Unpack[FaceitBanlistDefaultParams]) -> FaceitBanlistResponse: ...
    @overload
    def banlist_stats(self, **params: Unpack[FaceitBanlistStatsStreamParams]) -> BinaryIO: ...
    @overload
    def banlist_stats(self, **params: Unpack[FaceitBanlistStatsTextResponseParams]) -> str: ...
    @overload
    def banlist_stats(self, **params: Unpack[FaceitBanlistStatsDefaultParams]) -> FaceitBanlistStatsResponse: ...
    @overload
    def best_clips(self, **params: Unpack[FaceitBestClipsStreamParams]) -> BinaryIO: ...
    @overload
    def best_clips(self, **params: Unpack[FaceitBestClipsTextResponseParams]) -> str: ...
    @overload
    def best_clips(self, **params: Unpack[FaceitBestClipsDefaultParams]) -> FaceitBestClipsResponse: ...
    @overload
    def championship(self, **params: Unpack[FaceitChampionshipStreamParams]) -> BinaryIO: ...
    @overload
    def championship(self, **params: Unpack[FaceitChampionshipTextResponseParams]) -> str: ...
    @overload
    def championship(self, **params: Unpack[FaceitChampionshipDefaultParams]) -> FaceitChampionshipResponse: ...
    @overload
    def championship_bracket(self, **params: Unpack[FaceitChampionshipBracketStreamParams]) -> BinaryIO: ...
    @overload
    def championship_bracket(self, **params: Unpack[FaceitChampionshipBracketTextResponseParams]) -> str: ...
    @overload
    def championship_bracket(self, **params: Unpack[FaceitChampionshipBracketDefaultParams]) -> FaceitChampionshipBracketResponse: ...
    @overload
    def championship_participants(self, **params: Unpack[FaceitChampionshipParticipantsStreamParams]) -> BinaryIO: ...
    @overload
    def championship_participants(self, **params: Unpack[FaceitChampionshipParticipantsTextResponseParams]) -> str: ...
    @overload
    def championship_participants(self, **params: Unpack[FaceitChampionshipParticipantsDefaultParams]) -> FaceitChampionshipParticipantsResponse: ...
    @overload
    def championship_search(self, **params: Unpack[FaceitChampionshipSearchStreamParams]) -> BinaryIO: ...
    @overload
    def championship_search(self, **params: Unpack[FaceitChampionshipSearchTextResponseParams]) -> str: ...
    @overload
    def championship_search(self, **params: Unpack[FaceitChampionshipSearchDefaultParams]) -> FaceitChampionshipSearchResponse: ...
    @overload
    def clip(self, **params: Unpack[FaceitClipStreamParams]) -> BinaryIO: ...
    @overload
    def clip(self, **params: Unpack[FaceitClipTextResponseParams]) -> str: ...
    @overload
    def clip(self, **params: Unpack[FaceitClipDefaultParams]) -> FaceitClipResponse: ...
    @overload
    def clips(self, **params: Unpack[FaceitClipsStreamParams]) -> BinaryIO: ...
    @overload
    def clips(self, **params: Unpack[FaceitClipsTextResponseParams]) -> str: ...
    @overload
    def clips(self, **params: Unpack[FaceitClipsDefaultParams]) -> FaceitClipsResponse: ...
    @overload
    def competition_matches(self, **params: Unpack[FaceitCompetitionMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def competition_matches(self, **params: Unpack[FaceitCompetitionMatchesTextResponseParams]) -> str: ...
    @overload
    def competition_matches(self, **params: Unpack[FaceitCompetitionMatchesDefaultParams]) -> FaceitCompetitionMatchesResponse: ...
    @overload
    def fpl(self, **params: Unpack[FaceitFplStreamParams]) -> BinaryIO: ...
    @overload
    def fpl(self, **params: Unpack[FaceitFplTextResponseParams]) -> str: ...
    @overload
    def fpl(self, **params: Unpack[FaceitFplDefaultParams]) -> FaceitFplResponse: ...
    @overload
    def game_modes(self, **params: Unpack[FaceitGameModesStreamParams]) -> BinaryIO: ...
    @overload
    def game_modes(self, **params: Unpack[FaceitGameModesTextResponseParams]) -> str: ...
    @overload
    def game_modes(self, **params: Unpack[FaceitGameModesDefaultParams]) -> FaceitGameModesResponse: ...
    @overload
    def games(self, **params: Unpack[FaceitGamesStreamParams]) -> BinaryIO: ...
    @overload
    def games(self, **params: Unpack[FaceitGamesTextResponseParams]) -> str: ...
    @overload
    def games(self, **params: Unpack[FaceitGamesDefaultParams]) -> FaceitGamesResponse: ...
    @overload
    def hub(self, **params: Unpack[FaceitHubStreamParams]) -> BinaryIO: ...
    @overload
    def hub(self, **params: Unpack[FaceitHubTextResponseParams]) -> str: ...
    @overload
    def hub(self, **params: Unpack[FaceitHubDefaultParams]) -> FaceitHubResponse: ...
    @overload
    def hub_categories(self, **params: Unpack[FaceitHubCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def hub_categories(self, **params: Unpack[FaceitHubCategoriesTextResponseParams]) -> str: ...
    @overload
    def hub_categories(self, **params: Unpack[FaceitHubCategoriesDefaultParams]) -> FaceitHubCategoriesResponse: ...
    @overload
    def hub_memberships(self, **params: Unpack[FaceitHubMembershipsStreamParams]) -> BinaryIO: ...
    @overload
    def hub_memberships(self, **params: Unpack[FaceitHubMembershipsTextResponseParams]) -> str: ...
    @overload
    def hub_memberships(self, **params: Unpack[FaceitHubMembershipsDefaultParams]) -> FaceitHubMembershipsResponse: ...
    @overload
    def hubs(self, **params: Unpack[FaceitHubsStreamParams]) -> BinaryIO: ...
    @overload
    def hubs(self, **params: Unpack[FaceitHubsTextResponseParams]) -> str: ...
    @overload
    def hubs(self, **params: Unpack[FaceitHubsDefaultParams]) -> FaceitHubsResponse: ...
    @overload
    def hubs_detailed(self, **params: Unpack[FaceitHubsDetailedStreamParams]) -> BinaryIO: ...
    @overload
    def hubs_detailed(self, **params: Unpack[FaceitHubsDetailedTextResponseParams]) -> str: ...
    @overload
    def hubs_detailed(self, **params: Unpack[FaceitHubsDetailedDefaultParams]) -> FaceitHubsDetailedResponse: ...
    @overload
    def leaderboard(self, **params: Unpack[FaceitLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    def leaderboard(self, **params: Unpack[FaceitLeaderboardTextResponseParams]) -> str: ...
    @overload
    def leaderboard(self, **params: Unpack[FaceitLeaderboardDefaultParams]) -> FaceitLeaderboardResponse: ...
    @overload
    def leaderboard_detail(self, **params: Unpack[FaceitLeaderboardDetailStreamParams]) -> BinaryIO: ...
    @overload
    def leaderboard_detail(self, **params: Unpack[FaceitLeaderboardDetailTextResponseParams]) -> str: ...
    @overload
    def leaderboard_detail(self, **params: Unpack[FaceitLeaderboardDetailDefaultParams]) -> FaceitLeaderboardDetailResponse: ...
    @overload
    def leaderboard_statuses(self, **params: Unpack[FaceitLeaderboardStatusesStreamParams]) -> BinaryIO: ...
    @overload
    def leaderboard_statuses(self, **params: Unpack[FaceitLeaderboardStatusesTextResponseParams]) -> str: ...
    @overload
    def leaderboard_statuses(self, **params: Unpack[FaceitLeaderboardStatusesDefaultParams]) -> FaceitLeaderboardStatusesResponse: ...
    @overload
    def maps(self, **params: Unpack[FaceitMapsStreamParams]) -> BinaryIO: ...
    @overload
    def maps(self, **params: Unpack[FaceitMapsTextResponseParams]) -> str: ...
    @overload
    def maps(self, **params: Unpack[FaceitMapsDefaultParams]) -> FaceitMapsResponse: ...
    @overload
    def match_clips(self, **params: Unpack[FaceitMatchClipsStreamParams]) -> BinaryIO: ...
    @overload
    def match_clips(self, **params: Unpack[FaceitMatchClipsTextResponseParams]) -> str: ...
    @overload
    def match_clips(self, **params: Unpack[FaceitMatchClipsDefaultParams]) -> FaceitMatchClipsResponse: ...
    @overload
    def organizer(self, **params: Unpack[FaceitOrganizerStreamParams]) -> BinaryIO: ...
    @overload
    def organizer(self, **params: Unpack[FaceitOrganizerTextResponseParams]) -> str: ...
    @overload
    def organizer(self, **params: Unpack[FaceitOrganizerDefaultParams]) -> FaceitOrganizerResponse: ...
    @overload
    def player(self, **params: Unpack[FaceitPlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[FaceitPlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[FaceitPlayerDefaultParams]) -> FaceitPlayerResponse: ...
    @overload
    def player_rank(self, **params: Unpack[FaceitPlayerRankStreamParams]) -> BinaryIO: ...
    @overload
    def player_rank(self, **params: Unpack[FaceitPlayerRankTextResponseParams]) -> str: ...
    @overload
    def player_rank(self, **params: Unpack[FaceitPlayerRankDefaultParams]) -> FaceitPlayerRankResponse: ...
    @overload
    def regions(self, **params: Unpack[FaceitRegionsStreamParams]) -> BinaryIO: ...
    @overload
    def regions(self, **params: Unpack[FaceitRegionsTextResponseParams]) -> str: ...
    @overload
    def regions(self, **params: Unpack[FaceitRegionsDefaultParams]) -> FaceitRegionsResponse: ...
    @overload
    def rule(self, **params: Unpack[FaceitRuleStreamParams]) -> BinaryIO: ...
    @overload
    def rule(self, **params: Unpack[FaceitRuleTextResponseParams]) -> str: ...
    @overload
    def rule(self, **params: Unpack[FaceitRuleDefaultParams]) -> FaceitRuleResponse: ...
    @overload
    def rules(self, **params: Unpack[FaceitRulesStreamParams]) -> BinaryIO: ...
    @overload
    def rules(self, **params: Unpack[FaceitRulesTextResponseParams]) -> str: ...
    @overload
    def rules(self, **params: Unpack[FaceitRulesDefaultParams]) -> FaceitRulesResponse: ...
    @overload
    def skill_levels(self, **params: Unpack[FaceitSkillLevelsStreamParams]) -> BinaryIO: ...
    @overload
    def skill_levels(self, **params: Unpack[FaceitSkillLevelsTextResponseParams]) -> str: ...
    @overload
    def skill_levels(self, **params: Unpack[FaceitSkillLevelsDefaultParams]) -> FaceitSkillLevelsResponse: ...
    @overload
    def standings(self, **params: Unpack[FaceitStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def standings(self, **params: Unpack[FaceitStandingsTextResponseParams]) -> str: ...
    @overload
    def standings(self, **params: Unpack[FaceitStandingsDefaultParams]) -> FaceitStandingsResponse: ...
    @overload
    def team(self, **params: Unpack[FaceitTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[FaceitTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[FaceitTeamDefaultParams]) -> FaceitTeamResponse: ...
    @overload
    def tournaments_past(self, **params: Unpack[FaceitTournamentsPastStreamParams]) -> BinaryIO: ...
    @overload
    def tournaments_past(self, **params: Unpack[FaceitTournamentsPastTextResponseParams]) -> str: ...
    @overload
    def tournaments_past(self, **params: Unpack[FaceitTournamentsPastDefaultParams]) -> FaceitTournamentsPastResponse: ...
    @overload
    def user_skills(self, **params: Unpack[FaceitUserSkillsStreamParams]) -> BinaryIO: ...
    @overload
    def user_skills(self, **params: Unpack[FaceitUserSkillsTextResponseParams]) -> str: ...
    @overload
    def user_skills(self, **params: Unpack[FaceitUserSkillsDefaultParams]) -> FaceitUserSkillsResponse: ...

OperationId = Literal[
    'faceit-ban-reasons',
    'faceit-banlist',
    'faceit-banlist-stats',
    'faceit-best-clips',
    'faceit-championship',
    'faceit-championship-bracket',
    'faceit-championship-participants',
    'faceit-championship-search',
    'faceit-clip',
    'faceit-clips',
    'faceit-competition-matches',
    'faceit-fpl',
    'faceit-game-modes',
    'faceit-games',
    'faceit-hub',
    'faceit-hub-categories',
    'faceit-hub-memberships',
    'faceit-hubs',
    'faceit-hubs-detailed',
    'faceit-leaderboard',
    'faceit-leaderboard-detail',
    'faceit-leaderboard-statuses',
    'faceit-maps',
    'faceit-match-clips',
    'faceit-organizer',
    'faceit-player',
    'faceit-player-rank',
    'faceit-regions',
    'faceit-rule',
    'faceit-rules',
    'faceit-skill-levels',
    'faceit-standings',
    'faceit-team',
    'faceit-tournaments-past',
    'faceit-user-skills',
]

class CrawloraClient:
    faceit: FaceitGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-ban-reasons'],
        params: FaceitBanReasonsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitBanReasonsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-banlist'],
        params: FaceitBanlistParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitBanlistResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-banlist-stats'],
        params: FaceitBanlistStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitBanlistStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-best-clips'],
        params: FaceitBestClipsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitBestClipsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-championship'],
        params: FaceitChampionshipParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitChampionshipResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-championship-bracket'],
        params: FaceitChampionshipBracketParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitChampionshipBracketResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-championship-participants'],
        params: FaceitChampionshipParticipantsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitChampionshipParticipantsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-championship-search'],
        params: FaceitChampionshipSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitChampionshipSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-clip'],
        params: FaceitClipParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitClipResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-clips'],
        params: FaceitClipsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitClipsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-competition-matches'],
        params: FaceitCompetitionMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitCompetitionMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-fpl'],
        params: FaceitFplParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitFplResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-game-modes'],
        params: FaceitGameModesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitGameModesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-games'],
        params: FaceitGamesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitGamesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-hub'],
        params: FaceitHubParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitHubResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-hub-categories'],
        params: FaceitHubCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitHubCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-hub-memberships'],
        params: FaceitHubMembershipsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitHubMembershipsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-hubs'],
        params: FaceitHubsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitHubsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-hubs-detailed'],
        params: FaceitHubsDetailedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitHubsDetailedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-leaderboard'],
        params: FaceitLeaderboardParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitLeaderboardResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-leaderboard-detail'],
        params: FaceitLeaderboardDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitLeaderboardDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-leaderboard-statuses'],
        params: FaceitLeaderboardStatusesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitLeaderboardStatusesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-maps'],
        params: FaceitMapsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitMapsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-match-clips'],
        params: FaceitMatchClipsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitMatchClipsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-organizer'],
        params: FaceitOrganizerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitOrganizerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-player'],
        params: FaceitPlayerParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitPlayerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-player-rank'],
        params: FaceitPlayerRankParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitPlayerRankResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-regions'],
        params: FaceitRegionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitRegionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-rule'],
        params: FaceitRuleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitRuleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-rules'],
        params: FaceitRulesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitRulesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-skill-levels'],
        params: FaceitSkillLevelsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitSkillLevelsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-standings'],
        params: FaceitStandingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitStandingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-team'],
        params: FaceitTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitTeamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-tournaments-past'],
        params: FaceitTournamentsPastParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitTournamentsPastResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['faceit-user-skills'],
        params: FaceitUserSkillsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitUserSkillsResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-ban-reasons'],
        params: FaceitBanReasonsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitBanReasonsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-banlist'],
        params: FaceitBanlistParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitBanlistResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-banlist-stats'],
        params: FaceitBanlistStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitBanlistStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-best-clips'],
        params: FaceitBestClipsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitBestClipsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-championship'],
        params: FaceitChampionshipParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitChampionshipResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-championship-bracket'],
        params: FaceitChampionshipBracketParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitChampionshipBracketResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-championship-participants'],
        params: FaceitChampionshipParticipantsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitChampionshipParticipantsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-championship-search'],
        params: FaceitChampionshipSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitChampionshipSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-clip'],
        params: FaceitClipParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitClipResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-clips'],
        params: FaceitClipsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitClipsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-competition-matches'],
        params: FaceitCompetitionMatchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitCompetitionMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-fpl'],
        params: FaceitFplParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitFplResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-game-modes'],
        params: FaceitGameModesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitGameModesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-games'],
        params: FaceitGamesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitGamesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-hub'],
        params: FaceitHubParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitHubResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-hub-categories'],
        params: FaceitHubCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitHubCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-hub-memberships'],
        params: FaceitHubMembershipsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitHubMembershipsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-hubs'],
        params: FaceitHubsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitHubsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-hubs-detailed'],
        params: FaceitHubsDetailedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitHubsDetailedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-leaderboard'],
        params: FaceitLeaderboardParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitLeaderboardResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-leaderboard-detail'],
        params: FaceitLeaderboardDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitLeaderboardDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-leaderboard-statuses'],
        params: FaceitLeaderboardStatusesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitLeaderboardStatusesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-maps'],
        params: FaceitMapsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitMapsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-match-clips'],
        params: FaceitMatchClipsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitMatchClipsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-organizer'],
        params: FaceitOrganizerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitOrganizerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-player'],
        params: FaceitPlayerParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitPlayerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-player-rank'],
        params: FaceitPlayerRankParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitPlayerRankResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-regions'],
        params: FaceitRegionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitRegionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-rule'],
        params: FaceitRuleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitRuleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-rules'],
        params: FaceitRulesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitRulesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-skill-levels'],
        params: FaceitSkillLevelsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitSkillLevelsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-standings'],
        params: FaceitStandingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitStandingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-team'],
        params: FaceitTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitTeamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-tournaments-past'],
        params: FaceitTournamentsPastParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitTournamentsPastResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['faceit-user-skills'],
        params: FaceitUserSkillsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FaceitUserSkillsResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class FaceitClient(CrawloraClient):
    def __enter__(self) -> FaceitClient: ...
    @overload
    def ban_reasons(self, **params: Unpack[FaceitBanReasonsStreamParams]) -> BinaryIO: ...
    @overload
    def ban_reasons(self, **params: Unpack[FaceitBanReasonsTextResponseParams]) -> str: ...
    @overload
    def ban_reasons(self, **params: Unpack[FaceitBanReasonsDefaultParams]) -> FaceitBanReasonsResponse: ...
    @overload
    def banlist(self, **params: Unpack[FaceitBanlistStreamParams]) -> BinaryIO: ...
    @overload
    def banlist(self, **params: Unpack[FaceitBanlistTextResponseParams]) -> str: ...
    @overload
    def banlist(self, **params: Unpack[FaceitBanlistDefaultParams]) -> FaceitBanlistResponse: ...
    @overload
    def banlist_stats(self, **params: Unpack[FaceitBanlistStatsStreamParams]) -> BinaryIO: ...
    @overload
    def banlist_stats(self, **params: Unpack[FaceitBanlistStatsTextResponseParams]) -> str: ...
    @overload
    def banlist_stats(self, **params: Unpack[FaceitBanlistStatsDefaultParams]) -> FaceitBanlistStatsResponse: ...
    @overload
    def best_clips(self, **params: Unpack[FaceitBestClipsStreamParams]) -> BinaryIO: ...
    @overload
    def best_clips(self, **params: Unpack[FaceitBestClipsTextResponseParams]) -> str: ...
    @overload
    def best_clips(self, **params: Unpack[FaceitBestClipsDefaultParams]) -> FaceitBestClipsResponse: ...
    @overload
    def championship(self, **params: Unpack[FaceitChampionshipStreamParams]) -> BinaryIO: ...
    @overload
    def championship(self, **params: Unpack[FaceitChampionshipTextResponseParams]) -> str: ...
    @overload
    def championship(self, **params: Unpack[FaceitChampionshipDefaultParams]) -> FaceitChampionshipResponse: ...
    @overload
    def championship_bracket(self, **params: Unpack[FaceitChampionshipBracketStreamParams]) -> BinaryIO: ...
    @overload
    def championship_bracket(self, **params: Unpack[FaceitChampionshipBracketTextResponseParams]) -> str: ...
    @overload
    def championship_bracket(self, **params: Unpack[FaceitChampionshipBracketDefaultParams]) -> FaceitChampionshipBracketResponse: ...
    @overload
    def championship_participants(self, **params: Unpack[FaceitChampionshipParticipantsStreamParams]) -> BinaryIO: ...
    @overload
    def championship_participants(self, **params: Unpack[FaceitChampionshipParticipantsTextResponseParams]) -> str: ...
    @overload
    def championship_participants(self, **params: Unpack[FaceitChampionshipParticipantsDefaultParams]) -> FaceitChampionshipParticipantsResponse: ...
    @overload
    def championship_search(self, **params: Unpack[FaceitChampionshipSearchStreamParams]) -> BinaryIO: ...
    @overload
    def championship_search(self, **params: Unpack[FaceitChampionshipSearchTextResponseParams]) -> str: ...
    @overload
    def championship_search(self, **params: Unpack[FaceitChampionshipSearchDefaultParams]) -> FaceitChampionshipSearchResponse: ...
    @overload
    def clip(self, **params: Unpack[FaceitClipStreamParams]) -> BinaryIO: ...
    @overload
    def clip(self, **params: Unpack[FaceitClipTextResponseParams]) -> str: ...
    @overload
    def clip(self, **params: Unpack[FaceitClipDefaultParams]) -> FaceitClipResponse: ...
    @overload
    def clips(self, **params: Unpack[FaceitClipsStreamParams]) -> BinaryIO: ...
    @overload
    def clips(self, **params: Unpack[FaceitClipsTextResponseParams]) -> str: ...
    @overload
    def clips(self, **params: Unpack[FaceitClipsDefaultParams]) -> FaceitClipsResponse: ...
    @overload
    def competition_matches(self, **params: Unpack[FaceitCompetitionMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def competition_matches(self, **params: Unpack[FaceitCompetitionMatchesTextResponseParams]) -> str: ...
    @overload
    def competition_matches(self, **params: Unpack[FaceitCompetitionMatchesDefaultParams]) -> FaceitCompetitionMatchesResponse: ...
    @overload
    def fpl(self, **params: Unpack[FaceitFplStreamParams]) -> BinaryIO: ...
    @overload
    def fpl(self, **params: Unpack[FaceitFplTextResponseParams]) -> str: ...
    @overload
    def fpl(self, **params: Unpack[FaceitFplDefaultParams]) -> FaceitFplResponse: ...
    @overload
    def game_modes(self, **params: Unpack[FaceitGameModesStreamParams]) -> BinaryIO: ...
    @overload
    def game_modes(self, **params: Unpack[FaceitGameModesTextResponseParams]) -> str: ...
    @overload
    def game_modes(self, **params: Unpack[FaceitGameModesDefaultParams]) -> FaceitGameModesResponse: ...
    @overload
    def games(self, **params: Unpack[FaceitGamesStreamParams]) -> BinaryIO: ...
    @overload
    def games(self, **params: Unpack[FaceitGamesTextResponseParams]) -> str: ...
    @overload
    def games(self, **params: Unpack[FaceitGamesDefaultParams]) -> FaceitGamesResponse: ...
    @overload
    def hub(self, **params: Unpack[FaceitHubStreamParams]) -> BinaryIO: ...
    @overload
    def hub(self, **params: Unpack[FaceitHubTextResponseParams]) -> str: ...
    @overload
    def hub(self, **params: Unpack[FaceitHubDefaultParams]) -> FaceitHubResponse: ...
    @overload
    def hub_categories(self, **params: Unpack[FaceitHubCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def hub_categories(self, **params: Unpack[FaceitHubCategoriesTextResponseParams]) -> str: ...
    @overload
    def hub_categories(self, **params: Unpack[FaceitHubCategoriesDefaultParams]) -> FaceitHubCategoriesResponse: ...
    @overload
    def hub_memberships(self, **params: Unpack[FaceitHubMembershipsStreamParams]) -> BinaryIO: ...
    @overload
    def hub_memberships(self, **params: Unpack[FaceitHubMembershipsTextResponseParams]) -> str: ...
    @overload
    def hub_memberships(self, **params: Unpack[FaceitHubMembershipsDefaultParams]) -> FaceitHubMembershipsResponse: ...
    @overload
    def hubs(self, **params: Unpack[FaceitHubsStreamParams]) -> BinaryIO: ...
    @overload
    def hubs(self, **params: Unpack[FaceitHubsTextResponseParams]) -> str: ...
    @overload
    def hubs(self, **params: Unpack[FaceitHubsDefaultParams]) -> FaceitHubsResponse: ...
    @overload
    def hubs_detailed(self, **params: Unpack[FaceitHubsDetailedStreamParams]) -> BinaryIO: ...
    @overload
    def hubs_detailed(self, **params: Unpack[FaceitHubsDetailedTextResponseParams]) -> str: ...
    @overload
    def hubs_detailed(self, **params: Unpack[FaceitHubsDetailedDefaultParams]) -> FaceitHubsDetailedResponse: ...
    @overload
    def leaderboard(self, **params: Unpack[FaceitLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    def leaderboard(self, **params: Unpack[FaceitLeaderboardTextResponseParams]) -> str: ...
    @overload
    def leaderboard(self, **params: Unpack[FaceitLeaderboardDefaultParams]) -> FaceitLeaderboardResponse: ...
    @overload
    def leaderboard_detail(self, **params: Unpack[FaceitLeaderboardDetailStreamParams]) -> BinaryIO: ...
    @overload
    def leaderboard_detail(self, **params: Unpack[FaceitLeaderboardDetailTextResponseParams]) -> str: ...
    @overload
    def leaderboard_detail(self, **params: Unpack[FaceitLeaderboardDetailDefaultParams]) -> FaceitLeaderboardDetailResponse: ...
    @overload
    def leaderboard_statuses(self, **params: Unpack[FaceitLeaderboardStatusesStreamParams]) -> BinaryIO: ...
    @overload
    def leaderboard_statuses(self, **params: Unpack[FaceitLeaderboardStatusesTextResponseParams]) -> str: ...
    @overload
    def leaderboard_statuses(self, **params: Unpack[FaceitLeaderboardStatusesDefaultParams]) -> FaceitLeaderboardStatusesResponse: ...
    @overload
    def maps(self, **params: Unpack[FaceitMapsStreamParams]) -> BinaryIO: ...
    @overload
    def maps(self, **params: Unpack[FaceitMapsTextResponseParams]) -> str: ...
    @overload
    def maps(self, **params: Unpack[FaceitMapsDefaultParams]) -> FaceitMapsResponse: ...
    @overload
    def match_clips(self, **params: Unpack[FaceitMatchClipsStreamParams]) -> BinaryIO: ...
    @overload
    def match_clips(self, **params: Unpack[FaceitMatchClipsTextResponseParams]) -> str: ...
    @overload
    def match_clips(self, **params: Unpack[FaceitMatchClipsDefaultParams]) -> FaceitMatchClipsResponse: ...
    @overload
    def organizer(self, **params: Unpack[FaceitOrganizerStreamParams]) -> BinaryIO: ...
    @overload
    def organizer(self, **params: Unpack[FaceitOrganizerTextResponseParams]) -> str: ...
    @overload
    def organizer(self, **params: Unpack[FaceitOrganizerDefaultParams]) -> FaceitOrganizerResponse: ...
    @overload
    def player(self, **params: Unpack[FaceitPlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[FaceitPlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[FaceitPlayerDefaultParams]) -> FaceitPlayerResponse: ...
    @overload
    def player_rank(self, **params: Unpack[FaceitPlayerRankStreamParams]) -> BinaryIO: ...
    @overload
    def player_rank(self, **params: Unpack[FaceitPlayerRankTextResponseParams]) -> str: ...
    @overload
    def player_rank(self, **params: Unpack[FaceitPlayerRankDefaultParams]) -> FaceitPlayerRankResponse: ...
    @overload
    def regions(self, **params: Unpack[FaceitRegionsStreamParams]) -> BinaryIO: ...
    @overload
    def regions(self, **params: Unpack[FaceitRegionsTextResponseParams]) -> str: ...
    @overload
    def regions(self, **params: Unpack[FaceitRegionsDefaultParams]) -> FaceitRegionsResponse: ...
    @overload
    def rule(self, **params: Unpack[FaceitRuleStreamParams]) -> BinaryIO: ...
    @overload
    def rule(self, **params: Unpack[FaceitRuleTextResponseParams]) -> str: ...
    @overload
    def rule(self, **params: Unpack[FaceitRuleDefaultParams]) -> FaceitRuleResponse: ...
    @overload
    def rules(self, **params: Unpack[FaceitRulesStreamParams]) -> BinaryIO: ...
    @overload
    def rules(self, **params: Unpack[FaceitRulesTextResponseParams]) -> str: ...
    @overload
    def rules(self, **params: Unpack[FaceitRulesDefaultParams]) -> FaceitRulesResponse: ...
    @overload
    def skill_levels(self, **params: Unpack[FaceitSkillLevelsStreamParams]) -> BinaryIO: ...
    @overload
    def skill_levels(self, **params: Unpack[FaceitSkillLevelsTextResponseParams]) -> str: ...
    @overload
    def skill_levels(self, **params: Unpack[FaceitSkillLevelsDefaultParams]) -> FaceitSkillLevelsResponse: ...
    @overload
    def standings(self, **params: Unpack[FaceitStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def standings(self, **params: Unpack[FaceitStandingsTextResponseParams]) -> str: ...
    @overload
    def standings(self, **params: Unpack[FaceitStandingsDefaultParams]) -> FaceitStandingsResponse: ...
    @overload
    def team(self, **params: Unpack[FaceitTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[FaceitTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[FaceitTeamDefaultParams]) -> FaceitTeamResponse: ...
    @overload
    def tournaments_past(self, **params: Unpack[FaceitTournamentsPastStreamParams]) -> BinaryIO: ...
    @overload
    def tournaments_past(self, **params: Unpack[FaceitTournamentsPastTextResponseParams]) -> str: ...
    @overload
    def tournaments_past(self, **params: Unpack[FaceitTournamentsPastDefaultParams]) -> FaceitTournamentsPastResponse: ...
    @overload
    def user_skills(self, **params: Unpack[FaceitUserSkillsStreamParams]) -> BinaryIO: ...
    @overload
    def user_skills(self, **params: Unpack[FaceitUserSkillsTextResponseParams]) -> str: ...
    @overload
    def user_skills(self, **params: Unpack[FaceitUserSkillsDefaultParams]) -> FaceitUserSkillsResponse: ...

class AsyncFaceitClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncFaceitClient: ...
    faceit: _AsyncFaceitGroup
    @overload
    async def ban_reasons(self, **params: Unpack[FaceitBanReasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def ban_reasons(self, **params: Unpack[FaceitBanReasonsTextResponseParams]) -> str: ...
    @overload
    async def ban_reasons(self, **params: Unpack[FaceitBanReasonsDefaultParams]) -> FaceitBanReasonsResponse: ...
    @overload
    async def banlist(self, **params: Unpack[FaceitBanlistStreamParams]) -> BinaryIO: ...
    @overload
    async def banlist(self, **params: Unpack[FaceitBanlistTextResponseParams]) -> str: ...
    @overload
    async def banlist(self, **params: Unpack[FaceitBanlistDefaultParams]) -> FaceitBanlistResponse: ...
    @overload
    async def banlist_stats(self, **params: Unpack[FaceitBanlistStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def banlist_stats(self, **params: Unpack[FaceitBanlistStatsTextResponseParams]) -> str: ...
    @overload
    async def banlist_stats(self, **params: Unpack[FaceitBanlistStatsDefaultParams]) -> FaceitBanlistStatsResponse: ...
    @overload
    async def best_clips(self, **params: Unpack[FaceitBestClipsStreamParams]) -> BinaryIO: ...
    @overload
    async def best_clips(self, **params: Unpack[FaceitBestClipsTextResponseParams]) -> str: ...
    @overload
    async def best_clips(self, **params: Unpack[FaceitBestClipsDefaultParams]) -> FaceitBestClipsResponse: ...
    @overload
    async def championship(self, **params: Unpack[FaceitChampionshipStreamParams]) -> BinaryIO: ...
    @overload
    async def championship(self, **params: Unpack[FaceitChampionshipTextResponseParams]) -> str: ...
    @overload
    async def championship(self, **params: Unpack[FaceitChampionshipDefaultParams]) -> FaceitChampionshipResponse: ...
    @overload
    async def championship_bracket(self, **params: Unpack[FaceitChampionshipBracketStreamParams]) -> BinaryIO: ...
    @overload
    async def championship_bracket(self, **params: Unpack[FaceitChampionshipBracketTextResponseParams]) -> str: ...
    @overload
    async def championship_bracket(self, **params: Unpack[FaceitChampionshipBracketDefaultParams]) -> FaceitChampionshipBracketResponse: ...
    @overload
    async def championship_participants(self, **params: Unpack[FaceitChampionshipParticipantsStreamParams]) -> BinaryIO: ...
    @overload
    async def championship_participants(self, **params: Unpack[FaceitChampionshipParticipantsTextResponseParams]) -> str: ...
    @overload
    async def championship_participants(self, **params: Unpack[FaceitChampionshipParticipantsDefaultParams]) -> FaceitChampionshipParticipantsResponse: ...
    @overload
    async def championship_search(self, **params: Unpack[FaceitChampionshipSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def championship_search(self, **params: Unpack[FaceitChampionshipSearchTextResponseParams]) -> str: ...
    @overload
    async def championship_search(self, **params: Unpack[FaceitChampionshipSearchDefaultParams]) -> FaceitChampionshipSearchResponse: ...
    @overload
    async def clip(self, **params: Unpack[FaceitClipStreamParams]) -> BinaryIO: ...
    @overload
    async def clip(self, **params: Unpack[FaceitClipTextResponseParams]) -> str: ...
    @overload
    async def clip(self, **params: Unpack[FaceitClipDefaultParams]) -> FaceitClipResponse: ...
    @overload
    async def clips(self, **params: Unpack[FaceitClipsStreamParams]) -> BinaryIO: ...
    @overload
    async def clips(self, **params: Unpack[FaceitClipsTextResponseParams]) -> str: ...
    @overload
    async def clips(self, **params: Unpack[FaceitClipsDefaultParams]) -> FaceitClipsResponse: ...
    @overload
    async def competition_matches(self, **params: Unpack[FaceitCompetitionMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def competition_matches(self, **params: Unpack[FaceitCompetitionMatchesTextResponseParams]) -> str: ...
    @overload
    async def competition_matches(self, **params: Unpack[FaceitCompetitionMatchesDefaultParams]) -> FaceitCompetitionMatchesResponse: ...
    @overload
    async def fpl(self, **params: Unpack[FaceitFplStreamParams]) -> BinaryIO: ...
    @overload
    async def fpl(self, **params: Unpack[FaceitFplTextResponseParams]) -> str: ...
    @overload
    async def fpl(self, **params: Unpack[FaceitFplDefaultParams]) -> FaceitFplResponse: ...
    @overload
    async def game_modes(self, **params: Unpack[FaceitGameModesStreamParams]) -> BinaryIO: ...
    @overload
    async def game_modes(self, **params: Unpack[FaceitGameModesTextResponseParams]) -> str: ...
    @overload
    async def game_modes(self, **params: Unpack[FaceitGameModesDefaultParams]) -> FaceitGameModesResponse: ...
    @overload
    async def games(self, **params: Unpack[FaceitGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def games(self, **params: Unpack[FaceitGamesTextResponseParams]) -> str: ...
    @overload
    async def games(self, **params: Unpack[FaceitGamesDefaultParams]) -> FaceitGamesResponse: ...
    @overload
    async def hub(self, **params: Unpack[FaceitHubStreamParams]) -> BinaryIO: ...
    @overload
    async def hub(self, **params: Unpack[FaceitHubTextResponseParams]) -> str: ...
    @overload
    async def hub(self, **params: Unpack[FaceitHubDefaultParams]) -> FaceitHubResponse: ...
    @overload
    async def hub_categories(self, **params: Unpack[FaceitHubCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def hub_categories(self, **params: Unpack[FaceitHubCategoriesTextResponseParams]) -> str: ...
    @overload
    async def hub_categories(self, **params: Unpack[FaceitHubCategoriesDefaultParams]) -> FaceitHubCategoriesResponse: ...
    @overload
    async def hub_memberships(self, **params: Unpack[FaceitHubMembershipsStreamParams]) -> BinaryIO: ...
    @overload
    async def hub_memberships(self, **params: Unpack[FaceitHubMembershipsTextResponseParams]) -> str: ...
    @overload
    async def hub_memberships(self, **params: Unpack[FaceitHubMembershipsDefaultParams]) -> FaceitHubMembershipsResponse: ...
    @overload
    async def hubs(self, **params: Unpack[FaceitHubsStreamParams]) -> BinaryIO: ...
    @overload
    async def hubs(self, **params: Unpack[FaceitHubsTextResponseParams]) -> str: ...
    @overload
    async def hubs(self, **params: Unpack[FaceitHubsDefaultParams]) -> FaceitHubsResponse: ...
    @overload
    async def hubs_detailed(self, **params: Unpack[FaceitHubsDetailedStreamParams]) -> BinaryIO: ...
    @overload
    async def hubs_detailed(self, **params: Unpack[FaceitHubsDetailedTextResponseParams]) -> str: ...
    @overload
    async def hubs_detailed(self, **params: Unpack[FaceitHubsDetailedDefaultParams]) -> FaceitHubsDetailedResponse: ...
    @overload
    async def leaderboard(self, **params: Unpack[FaceitLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    async def leaderboard(self, **params: Unpack[FaceitLeaderboardTextResponseParams]) -> str: ...
    @overload
    async def leaderboard(self, **params: Unpack[FaceitLeaderboardDefaultParams]) -> FaceitLeaderboardResponse: ...
    @overload
    async def leaderboard_detail(self, **params: Unpack[FaceitLeaderboardDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def leaderboard_detail(self, **params: Unpack[FaceitLeaderboardDetailTextResponseParams]) -> str: ...
    @overload
    async def leaderboard_detail(self, **params: Unpack[FaceitLeaderboardDetailDefaultParams]) -> FaceitLeaderboardDetailResponse: ...
    @overload
    async def leaderboard_statuses(self, **params: Unpack[FaceitLeaderboardStatusesStreamParams]) -> BinaryIO: ...
    @overload
    async def leaderboard_statuses(self, **params: Unpack[FaceitLeaderboardStatusesTextResponseParams]) -> str: ...
    @overload
    async def leaderboard_statuses(self, **params: Unpack[FaceitLeaderboardStatusesDefaultParams]) -> FaceitLeaderboardStatusesResponse: ...
    @overload
    async def maps(self, **params: Unpack[FaceitMapsStreamParams]) -> BinaryIO: ...
    @overload
    async def maps(self, **params: Unpack[FaceitMapsTextResponseParams]) -> str: ...
    @overload
    async def maps(self, **params: Unpack[FaceitMapsDefaultParams]) -> FaceitMapsResponse: ...
    @overload
    async def match_clips(self, **params: Unpack[FaceitMatchClipsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_clips(self, **params: Unpack[FaceitMatchClipsTextResponseParams]) -> str: ...
    @overload
    async def match_clips(self, **params: Unpack[FaceitMatchClipsDefaultParams]) -> FaceitMatchClipsResponse: ...
    @overload
    async def organizer(self, **params: Unpack[FaceitOrganizerStreamParams]) -> BinaryIO: ...
    @overload
    async def organizer(self, **params: Unpack[FaceitOrganizerTextResponseParams]) -> str: ...
    @overload
    async def organizer(self, **params: Unpack[FaceitOrganizerDefaultParams]) -> FaceitOrganizerResponse: ...
    @overload
    async def player(self, **params: Unpack[FaceitPlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[FaceitPlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[FaceitPlayerDefaultParams]) -> FaceitPlayerResponse: ...
    @overload
    async def player_rank(self, **params: Unpack[FaceitPlayerRankStreamParams]) -> BinaryIO: ...
    @overload
    async def player_rank(self, **params: Unpack[FaceitPlayerRankTextResponseParams]) -> str: ...
    @overload
    async def player_rank(self, **params: Unpack[FaceitPlayerRankDefaultParams]) -> FaceitPlayerRankResponse: ...
    @overload
    async def regions(self, **params: Unpack[FaceitRegionsStreamParams]) -> BinaryIO: ...
    @overload
    async def regions(self, **params: Unpack[FaceitRegionsTextResponseParams]) -> str: ...
    @overload
    async def regions(self, **params: Unpack[FaceitRegionsDefaultParams]) -> FaceitRegionsResponse: ...
    @overload
    async def rule(self, **params: Unpack[FaceitRuleStreamParams]) -> BinaryIO: ...
    @overload
    async def rule(self, **params: Unpack[FaceitRuleTextResponseParams]) -> str: ...
    @overload
    async def rule(self, **params: Unpack[FaceitRuleDefaultParams]) -> FaceitRuleResponse: ...
    @overload
    async def rules(self, **params: Unpack[FaceitRulesStreamParams]) -> BinaryIO: ...
    @overload
    async def rules(self, **params: Unpack[FaceitRulesTextResponseParams]) -> str: ...
    @overload
    async def rules(self, **params: Unpack[FaceitRulesDefaultParams]) -> FaceitRulesResponse: ...
    @overload
    async def skill_levels(self, **params: Unpack[FaceitSkillLevelsStreamParams]) -> BinaryIO: ...
    @overload
    async def skill_levels(self, **params: Unpack[FaceitSkillLevelsTextResponseParams]) -> str: ...
    @overload
    async def skill_levels(self, **params: Unpack[FaceitSkillLevelsDefaultParams]) -> FaceitSkillLevelsResponse: ...
    @overload
    async def standings(self, **params: Unpack[FaceitStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def standings(self, **params: Unpack[FaceitStandingsTextResponseParams]) -> str: ...
    @overload
    async def standings(self, **params: Unpack[FaceitStandingsDefaultParams]) -> FaceitStandingsResponse: ...
    @overload
    async def team(self, **params: Unpack[FaceitTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[FaceitTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[FaceitTeamDefaultParams]) -> FaceitTeamResponse: ...
    @overload
    async def tournaments_past(self, **params: Unpack[FaceitTournamentsPastStreamParams]) -> BinaryIO: ...
    @overload
    async def tournaments_past(self, **params: Unpack[FaceitTournamentsPastTextResponseParams]) -> str: ...
    @overload
    async def tournaments_past(self, **params: Unpack[FaceitTournamentsPastDefaultParams]) -> FaceitTournamentsPastResponse: ...
    @overload
    async def user_skills(self, **params: Unpack[FaceitUserSkillsStreamParams]) -> BinaryIO: ...
    @overload
    async def user_skills(self, **params: Unpack[FaceitUserSkillsTextResponseParams]) -> str: ...
    @overload
    async def user_skills(self, **params: Unpack[FaceitUserSkillsDefaultParams]) -> FaceitUserSkillsResponse: ...

class _AsyncFaceitGroup:
    @overload
    async def ban_reasons(self, **params: Unpack[FaceitBanReasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def ban_reasons(self, **params: Unpack[FaceitBanReasonsTextResponseParams]) -> str: ...
    @overload
    async def ban_reasons(self, **params: Unpack[FaceitBanReasonsDefaultParams]) -> FaceitBanReasonsResponse: ...
    @overload
    async def banlist(self, **params: Unpack[FaceitBanlistStreamParams]) -> BinaryIO: ...
    @overload
    async def banlist(self, **params: Unpack[FaceitBanlistTextResponseParams]) -> str: ...
    @overload
    async def banlist(self, **params: Unpack[FaceitBanlistDefaultParams]) -> FaceitBanlistResponse: ...
    @overload
    async def banlist_stats(self, **params: Unpack[FaceitBanlistStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def banlist_stats(self, **params: Unpack[FaceitBanlistStatsTextResponseParams]) -> str: ...
    @overload
    async def banlist_stats(self, **params: Unpack[FaceitBanlistStatsDefaultParams]) -> FaceitBanlistStatsResponse: ...
    @overload
    async def best_clips(self, **params: Unpack[FaceitBestClipsStreamParams]) -> BinaryIO: ...
    @overload
    async def best_clips(self, **params: Unpack[FaceitBestClipsTextResponseParams]) -> str: ...
    @overload
    async def best_clips(self, **params: Unpack[FaceitBestClipsDefaultParams]) -> FaceitBestClipsResponse: ...
    @overload
    async def championship(self, **params: Unpack[FaceitChampionshipStreamParams]) -> BinaryIO: ...
    @overload
    async def championship(self, **params: Unpack[FaceitChampionshipTextResponseParams]) -> str: ...
    @overload
    async def championship(self, **params: Unpack[FaceitChampionshipDefaultParams]) -> FaceitChampionshipResponse: ...
    @overload
    async def championship_bracket(self, **params: Unpack[FaceitChampionshipBracketStreamParams]) -> BinaryIO: ...
    @overload
    async def championship_bracket(self, **params: Unpack[FaceitChampionshipBracketTextResponseParams]) -> str: ...
    @overload
    async def championship_bracket(self, **params: Unpack[FaceitChampionshipBracketDefaultParams]) -> FaceitChampionshipBracketResponse: ...
    @overload
    async def championship_participants(self, **params: Unpack[FaceitChampionshipParticipantsStreamParams]) -> BinaryIO: ...
    @overload
    async def championship_participants(self, **params: Unpack[FaceitChampionshipParticipantsTextResponseParams]) -> str: ...
    @overload
    async def championship_participants(self, **params: Unpack[FaceitChampionshipParticipantsDefaultParams]) -> FaceitChampionshipParticipantsResponse: ...
    @overload
    async def championship_search(self, **params: Unpack[FaceitChampionshipSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def championship_search(self, **params: Unpack[FaceitChampionshipSearchTextResponseParams]) -> str: ...
    @overload
    async def championship_search(self, **params: Unpack[FaceitChampionshipSearchDefaultParams]) -> FaceitChampionshipSearchResponse: ...
    @overload
    async def clip(self, **params: Unpack[FaceitClipStreamParams]) -> BinaryIO: ...
    @overload
    async def clip(self, **params: Unpack[FaceitClipTextResponseParams]) -> str: ...
    @overload
    async def clip(self, **params: Unpack[FaceitClipDefaultParams]) -> FaceitClipResponse: ...
    @overload
    async def clips(self, **params: Unpack[FaceitClipsStreamParams]) -> BinaryIO: ...
    @overload
    async def clips(self, **params: Unpack[FaceitClipsTextResponseParams]) -> str: ...
    @overload
    async def clips(self, **params: Unpack[FaceitClipsDefaultParams]) -> FaceitClipsResponse: ...
    @overload
    async def competition_matches(self, **params: Unpack[FaceitCompetitionMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def competition_matches(self, **params: Unpack[FaceitCompetitionMatchesTextResponseParams]) -> str: ...
    @overload
    async def competition_matches(self, **params: Unpack[FaceitCompetitionMatchesDefaultParams]) -> FaceitCompetitionMatchesResponse: ...
    @overload
    async def fpl(self, **params: Unpack[FaceitFplStreamParams]) -> BinaryIO: ...
    @overload
    async def fpl(self, **params: Unpack[FaceitFplTextResponseParams]) -> str: ...
    @overload
    async def fpl(self, **params: Unpack[FaceitFplDefaultParams]) -> FaceitFplResponse: ...
    @overload
    async def game_modes(self, **params: Unpack[FaceitGameModesStreamParams]) -> BinaryIO: ...
    @overload
    async def game_modes(self, **params: Unpack[FaceitGameModesTextResponseParams]) -> str: ...
    @overload
    async def game_modes(self, **params: Unpack[FaceitGameModesDefaultParams]) -> FaceitGameModesResponse: ...
    @overload
    async def games(self, **params: Unpack[FaceitGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def games(self, **params: Unpack[FaceitGamesTextResponseParams]) -> str: ...
    @overload
    async def games(self, **params: Unpack[FaceitGamesDefaultParams]) -> FaceitGamesResponse: ...
    @overload
    async def hub(self, **params: Unpack[FaceitHubStreamParams]) -> BinaryIO: ...
    @overload
    async def hub(self, **params: Unpack[FaceitHubTextResponseParams]) -> str: ...
    @overload
    async def hub(self, **params: Unpack[FaceitHubDefaultParams]) -> FaceitHubResponse: ...
    @overload
    async def hub_categories(self, **params: Unpack[FaceitHubCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def hub_categories(self, **params: Unpack[FaceitHubCategoriesTextResponseParams]) -> str: ...
    @overload
    async def hub_categories(self, **params: Unpack[FaceitHubCategoriesDefaultParams]) -> FaceitHubCategoriesResponse: ...
    @overload
    async def hub_memberships(self, **params: Unpack[FaceitHubMembershipsStreamParams]) -> BinaryIO: ...
    @overload
    async def hub_memberships(self, **params: Unpack[FaceitHubMembershipsTextResponseParams]) -> str: ...
    @overload
    async def hub_memberships(self, **params: Unpack[FaceitHubMembershipsDefaultParams]) -> FaceitHubMembershipsResponse: ...
    @overload
    async def hubs(self, **params: Unpack[FaceitHubsStreamParams]) -> BinaryIO: ...
    @overload
    async def hubs(self, **params: Unpack[FaceitHubsTextResponseParams]) -> str: ...
    @overload
    async def hubs(self, **params: Unpack[FaceitHubsDefaultParams]) -> FaceitHubsResponse: ...
    @overload
    async def hubs_detailed(self, **params: Unpack[FaceitHubsDetailedStreamParams]) -> BinaryIO: ...
    @overload
    async def hubs_detailed(self, **params: Unpack[FaceitHubsDetailedTextResponseParams]) -> str: ...
    @overload
    async def hubs_detailed(self, **params: Unpack[FaceitHubsDetailedDefaultParams]) -> FaceitHubsDetailedResponse: ...
    @overload
    async def leaderboard(self, **params: Unpack[FaceitLeaderboardStreamParams]) -> BinaryIO: ...
    @overload
    async def leaderboard(self, **params: Unpack[FaceitLeaderboardTextResponseParams]) -> str: ...
    @overload
    async def leaderboard(self, **params: Unpack[FaceitLeaderboardDefaultParams]) -> FaceitLeaderboardResponse: ...
    @overload
    async def leaderboard_detail(self, **params: Unpack[FaceitLeaderboardDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def leaderboard_detail(self, **params: Unpack[FaceitLeaderboardDetailTextResponseParams]) -> str: ...
    @overload
    async def leaderboard_detail(self, **params: Unpack[FaceitLeaderboardDetailDefaultParams]) -> FaceitLeaderboardDetailResponse: ...
    @overload
    async def leaderboard_statuses(self, **params: Unpack[FaceitLeaderboardStatusesStreamParams]) -> BinaryIO: ...
    @overload
    async def leaderboard_statuses(self, **params: Unpack[FaceitLeaderboardStatusesTextResponseParams]) -> str: ...
    @overload
    async def leaderboard_statuses(self, **params: Unpack[FaceitLeaderboardStatusesDefaultParams]) -> FaceitLeaderboardStatusesResponse: ...
    @overload
    async def maps(self, **params: Unpack[FaceitMapsStreamParams]) -> BinaryIO: ...
    @overload
    async def maps(self, **params: Unpack[FaceitMapsTextResponseParams]) -> str: ...
    @overload
    async def maps(self, **params: Unpack[FaceitMapsDefaultParams]) -> FaceitMapsResponse: ...
    @overload
    async def match_clips(self, **params: Unpack[FaceitMatchClipsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_clips(self, **params: Unpack[FaceitMatchClipsTextResponseParams]) -> str: ...
    @overload
    async def match_clips(self, **params: Unpack[FaceitMatchClipsDefaultParams]) -> FaceitMatchClipsResponse: ...
    @overload
    async def organizer(self, **params: Unpack[FaceitOrganizerStreamParams]) -> BinaryIO: ...
    @overload
    async def organizer(self, **params: Unpack[FaceitOrganizerTextResponseParams]) -> str: ...
    @overload
    async def organizer(self, **params: Unpack[FaceitOrganizerDefaultParams]) -> FaceitOrganizerResponse: ...
    @overload
    async def player(self, **params: Unpack[FaceitPlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[FaceitPlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[FaceitPlayerDefaultParams]) -> FaceitPlayerResponse: ...
    @overload
    async def player_rank(self, **params: Unpack[FaceitPlayerRankStreamParams]) -> BinaryIO: ...
    @overload
    async def player_rank(self, **params: Unpack[FaceitPlayerRankTextResponseParams]) -> str: ...
    @overload
    async def player_rank(self, **params: Unpack[FaceitPlayerRankDefaultParams]) -> FaceitPlayerRankResponse: ...
    @overload
    async def regions(self, **params: Unpack[FaceitRegionsStreamParams]) -> BinaryIO: ...
    @overload
    async def regions(self, **params: Unpack[FaceitRegionsTextResponseParams]) -> str: ...
    @overload
    async def regions(self, **params: Unpack[FaceitRegionsDefaultParams]) -> FaceitRegionsResponse: ...
    @overload
    async def rule(self, **params: Unpack[FaceitRuleStreamParams]) -> BinaryIO: ...
    @overload
    async def rule(self, **params: Unpack[FaceitRuleTextResponseParams]) -> str: ...
    @overload
    async def rule(self, **params: Unpack[FaceitRuleDefaultParams]) -> FaceitRuleResponse: ...
    @overload
    async def rules(self, **params: Unpack[FaceitRulesStreamParams]) -> BinaryIO: ...
    @overload
    async def rules(self, **params: Unpack[FaceitRulesTextResponseParams]) -> str: ...
    @overload
    async def rules(self, **params: Unpack[FaceitRulesDefaultParams]) -> FaceitRulesResponse: ...
    @overload
    async def skill_levels(self, **params: Unpack[FaceitSkillLevelsStreamParams]) -> BinaryIO: ...
    @overload
    async def skill_levels(self, **params: Unpack[FaceitSkillLevelsTextResponseParams]) -> str: ...
    @overload
    async def skill_levels(self, **params: Unpack[FaceitSkillLevelsDefaultParams]) -> FaceitSkillLevelsResponse: ...
    @overload
    async def standings(self, **params: Unpack[FaceitStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def standings(self, **params: Unpack[FaceitStandingsTextResponseParams]) -> str: ...
    @overload
    async def standings(self, **params: Unpack[FaceitStandingsDefaultParams]) -> FaceitStandingsResponse: ...
    @overload
    async def team(self, **params: Unpack[FaceitTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[FaceitTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[FaceitTeamDefaultParams]) -> FaceitTeamResponse: ...
    @overload
    async def tournaments_past(self, **params: Unpack[FaceitTournamentsPastStreamParams]) -> BinaryIO: ...
    @overload
    async def tournaments_past(self, **params: Unpack[FaceitTournamentsPastTextResponseParams]) -> str: ...
    @overload
    async def tournaments_past(self, **params: Unpack[FaceitTournamentsPastDefaultParams]) -> FaceitTournamentsPastResponse: ...
    @overload
    async def user_skills(self, **params: Unpack[FaceitUserSkillsStreamParams]) -> BinaryIO: ...
    @overload
    async def user_skills(self, **params: Unpack[FaceitUserSkillsTextResponseParams]) -> str: ...
    @overload
    async def user_skills(self, **params: Unpack[FaceitUserSkillsDefaultParams]) -> FaceitUserSkillsResponse: ...

FaceitBanReasonsDefaultParams = TypedDict('FaceitBanReasonsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FaceitBanReasonsTextResponseParams = TypedDict('FaceitBanReasonsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FaceitBanReasonsStreamParams = TypedDict('FaceitBanReasonsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FaceitBanlistDefaultParams = TypedDict('FaceitBanlistDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'size': NotRequired[int],
    'cursor': NotRequired[str],
    'reason': NotRequired[str],
}, total=False)

FaceitBanlistTextResponseParams = TypedDict('FaceitBanlistTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'size': NotRequired[int],
    'cursor': NotRequired[str],
    'reason': NotRequired[str],
}, total=False)

FaceitBanlistStreamParams = TypedDict('FaceitBanlistStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'size': NotRequired[int],
    'cursor': NotRequired[str],
    'reason': NotRequired[str],
}, total=False)

FaceitBanlistStatsDefaultParams = TypedDict('FaceitBanlistStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FaceitBanlistStatsTextResponseParams = TypedDict('FaceitBanlistStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FaceitBanlistStatsStreamParams = TypedDict('FaceitBanlistStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FaceitBestClipsDefaultParams = TypedDict('FaceitBestClipsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['cs2']],
    'user_id': Required[str],
    'from': Required[str],
    'to': Required[str],
    'limit': NotRequired[int],
}, total=False)

FaceitBestClipsTextResponseParams = TypedDict('FaceitBestClipsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['cs2']],
    'user_id': Required[str],
    'from': Required[str],
    'to': Required[str],
    'limit': NotRequired[int],
}, total=False)

FaceitBestClipsStreamParams = TypedDict('FaceitBestClipsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['cs2']],
    'user_id': Required[str],
    'from': Required[str],
    'to': Required[str],
    'limit': NotRequired[int],
}, total=False)

FaceitChampionshipDefaultParams = TypedDict('FaceitChampionshipDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FaceitChampionshipTextResponseParams = TypedDict('FaceitChampionshipTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FaceitChampionshipStreamParams = TypedDict('FaceitChampionshipStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FaceitChampionshipBracketDefaultParams = TypedDict('FaceitChampionshipBracketDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'group': Required[int],
    'round': Required[int],
    'start': NotRequired[int],
    'end': NotRequired[int],
}, total=False)

FaceitChampionshipBracketTextResponseParams = TypedDict('FaceitChampionshipBracketTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'group': Required[int],
    'round': Required[int],
    'start': NotRequired[int],
    'end': NotRequired[int],
}, total=False)

FaceitChampionshipBracketStreamParams = TypedDict('FaceitChampionshipBracketStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'group': Required[int],
    'round': Required[int],
    'start': NotRequired[int],
    'end': NotRequired[int],
}, total=False)

FaceitChampionshipParticipantsDefaultParams = TypedDict('FaceitChampionshipParticipantsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitChampionshipParticipantsTextResponseParams = TypedDict('FaceitChampionshipParticipantsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitChampionshipParticipantsStreamParams = TypedDict('FaceitChampionshipParticipantsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitChampionshipSearchDefaultParams = TypedDict('FaceitChampionshipSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'entity_type': NotRequired[str],
    'type': NotRequired[str],
    'status': NotRequired[Literal['ONGOING', 'UPCOMING', 'FINISHED']],
    'subtype': NotRequired[str],
    'country': NotRequired[str],
    'game': NotRequired[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'has_drops': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitChampionshipSearchTextResponseParams = TypedDict('FaceitChampionshipSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'entity_type': NotRequired[str],
    'type': NotRequired[str],
    'status': NotRequired[Literal['ONGOING', 'UPCOMING', 'FINISHED']],
    'subtype': NotRequired[str],
    'country': NotRequired[str],
    'game': NotRequired[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'has_drops': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitChampionshipSearchStreamParams = TypedDict('FaceitChampionshipSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'entity_type': NotRequired[str],
    'type': NotRequired[str],
    'status': NotRequired[Literal['ONGOING', 'UPCOMING', 'FINISHED']],
    'subtype': NotRequired[str],
    'country': NotRequired[str],
    'game': NotRequired[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'has_drops': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitClipDefaultParams = TypedDict('FaceitClipDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FaceitClipTextResponseParams = TypedDict('FaceitClipTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FaceitClipStreamParams = TypedDict('FaceitClipStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FaceitClipsDefaultParams = TypedDict('FaceitClipsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['cs2']],
    'user_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitClipsTextResponseParams = TypedDict('FaceitClipsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['cs2']],
    'user_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitClipsStreamParams = TypedDict('FaceitClipsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['cs2']],
    'user_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitCompetitionMatchesDefaultParams = TypedDict('FaceitCompetitionMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'type': Required[str],
    'player_id': NotRequired[str],
    'page': NotRequired[int],
    'size': NotRequired[int],
}, total=False)

FaceitCompetitionMatchesTextResponseParams = TypedDict('FaceitCompetitionMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'type': Required[str],
    'player_id': NotRequired[str],
    'page': NotRequired[int],
    'size': NotRequired[int],
}, total=False)

FaceitCompetitionMatchesStreamParams = TypedDict('FaceitCompetitionMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'type': Required[str],
    'player_id': NotRequired[str],
    'page': NotRequired[int],
    'size': NotRequired[int],
}, total=False)

FaceitFplDefaultParams = TypedDict('FaceitFplDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitFplTextResponseParams = TypedDict('FaceitFplTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitFplStreamParams = TypedDict('FaceitFplStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitGameModesDefaultParams = TypedDict('FaceitGameModesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'region': Required[str],
}, total=False)

FaceitGameModesTextResponseParams = TypedDict('FaceitGameModesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'region': Required[str],
}, total=False)

FaceitGameModesStreamParams = TypedDict('FaceitGameModesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'region': Required[str],
}, total=False)

FaceitGamesDefaultParams = TypedDict('FaceitGamesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FaceitGamesTextResponseParams = TypedDict('FaceitGamesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FaceitGamesStreamParams = TypedDict('FaceitGamesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FaceitHubDefaultParams = TypedDict('FaceitHubDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FaceitHubTextResponseParams = TypedDict('FaceitHubTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FaceitHubStreamParams = TypedDict('FaceitHubStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FaceitHubCategoriesDefaultParams = TypedDict('FaceitHubCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FaceitHubCategoriesTextResponseParams = TypedDict('FaceitHubCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FaceitHubCategoriesStreamParams = TypedDict('FaceitHubCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FaceitHubMembershipsDefaultParams = TypedDict('FaceitHubMembershipsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': Required[str],
    'category': NotRequired[Literal['community', 'chat', 'ihl']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitHubMembershipsTextResponseParams = TypedDict('FaceitHubMembershipsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': Required[str],
    'category': NotRequired[Literal['community', 'chat', 'ihl']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitHubMembershipsStreamParams = TypedDict('FaceitHubMembershipsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': Required[str],
    'category': NotRequired[Literal['community', 'chat', 'ihl']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitHubsDefaultParams = TypedDict('FaceitHubsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'ids': Required[list[str]],
}, total=False)

FaceitHubsTextResponseParams = TypedDict('FaceitHubsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'ids': Required[list[str]],
}, total=False)

FaceitHubsStreamParams = TypedDict('FaceitHubsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'ids': Required[list[str]],
}, total=False)

FaceitHubsDetailedDefaultParams = TypedDict('FaceitHubsDetailedDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'ids': Required[list[str]],
}, total=False)

FaceitHubsDetailedTextResponseParams = TypedDict('FaceitHubsDetailedTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'ids': Required[list[str]],
}, total=False)

FaceitHubsDetailedStreamParams = TypedDict('FaceitHubsDetailedStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'ids': Required[list[str]],
}, total=False)

FaceitLeaderboardDefaultParams = TypedDict('FaceitLeaderboardDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'region': Required[str],
    'season': NotRequired[int],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitLeaderboardTextResponseParams = TypedDict('FaceitLeaderboardTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'region': Required[str],
    'season': NotRequired[int],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitLeaderboardStreamParams = TypedDict('FaceitLeaderboardStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'region': Required[str],
    'season': NotRequired[int],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitLeaderboardDetailDefaultParams = TypedDict('FaceitLeaderboardDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FaceitLeaderboardDetailTextResponseParams = TypedDict('FaceitLeaderboardDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FaceitLeaderboardDetailStreamParams = TypedDict('FaceitLeaderboardDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FaceitLeaderboardStatusesDefaultParams = TypedDict('FaceitLeaderboardStatusesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FaceitLeaderboardStatusesTextResponseParams = TypedDict('FaceitLeaderboardStatusesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FaceitLeaderboardStatusesStreamParams = TypedDict('FaceitLeaderboardStatusesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FaceitMapsDefaultParams = TypedDict('FaceitMapsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
}, total=False)

FaceitMapsTextResponseParams = TypedDict('FaceitMapsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
}, total=False)

FaceitMapsStreamParams = TypedDict('FaceitMapsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
}, total=False)

FaceitMatchClipsDefaultParams = TypedDict('FaceitMatchClipsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['cs2']],
    'match_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitMatchClipsTextResponseParams = TypedDict('FaceitMatchClipsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['cs2']],
    'match_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitMatchClipsStreamParams = TypedDict('FaceitMatchClipsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['cs2']],
    'match_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitOrganizerDefaultParams = TypedDict('FaceitOrganizerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FaceitOrganizerTextResponseParams = TypedDict('FaceitOrganizerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FaceitOrganizerStreamParams = TypedDict('FaceitOrganizerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FaceitPlayerDefaultParams = TypedDict('FaceitPlayerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'nickname': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

FaceitPlayerTextResponseParams = TypedDict('FaceitPlayerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'nickname': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

FaceitPlayerStreamParams = TypedDict('FaceitPlayerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'nickname': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

FaceitPlayerRankDefaultParams = TypedDict('FaceitPlayerRankDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'region': Required[str],
    'nickname': NotRequired[str],
    'user_id': NotRequired[str],
    'season': NotRequired[int],
}, total=False)

FaceitPlayerRankTextResponseParams = TypedDict('FaceitPlayerRankTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'region': Required[str],
    'nickname': NotRequired[str],
    'user_id': NotRequired[str],
    'season': NotRequired[int],
}, total=False)

FaceitPlayerRankStreamParams = TypedDict('FaceitPlayerRankStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
    'region': Required[str],
    'nickname': NotRequired[str],
    'user_id': NotRequired[str],
    'season': NotRequired[int],
}, total=False)

FaceitRegionsDefaultParams = TypedDict('FaceitRegionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FaceitRegionsTextResponseParams = TypedDict('FaceitRegionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FaceitRegionsStreamParams = TypedDict('FaceitRegionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FaceitRuleDefaultParams = TypedDict('FaceitRuleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FaceitRuleTextResponseParams = TypedDict('FaceitRuleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FaceitRuleStreamParams = TypedDict('FaceitRuleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FaceitRulesDefaultParams = TypedDict('FaceitRulesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitRulesTextResponseParams = TypedDict('FaceitRulesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitRulesStreamParams = TypedDict('FaceitRulesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitSkillLevelsDefaultParams = TypedDict('FaceitSkillLevelsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
}, total=False)

FaceitSkillLevelsTextResponseParams = TypedDict('FaceitSkillLevelsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
}, total=False)

FaceitSkillLevelsStreamParams = TypedDict('FaceitSkillLevelsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['cs2', 'csgo', 'ow2', 'valorant', 'pubg', 'tf2', 'krunker', 'pubgmobile', 'apex', 'fortnite', 'wow', 'brawl_stars', 'insidia', 'dota2', 'hearthstone', 'wildrift', 'clash_royale', 'smite', 'lol_NA', 'lol_EUW', 'lol_EUN', 'overwatch_EU', 'wot_EU', 'wot_RU', 'rainbow_6', 'csdz', 'battalion']],
}, total=False)

FaceitStandingsDefaultParams = TypedDict('FaceitStandingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'entity_id': Required[str],
    'group': Required[int],
    'round': Required[str],
    'segment': NotRequired[int],
    'match': NotRequired[int],
}, total=False)

FaceitStandingsTextResponseParams = TypedDict('FaceitStandingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'entity_id': Required[str],
    'group': Required[int],
    'round': Required[str],
    'segment': NotRequired[int],
    'match': NotRequired[int],
}, total=False)

FaceitStandingsStreamParams = TypedDict('FaceitStandingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'entity_id': Required[str],
    'group': Required[int],
    'round': Required[str],
    'segment': NotRequired[int],
    'match': NotRequired[int],
}, total=False)

FaceitTeamDefaultParams = TypedDict('FaceitTeamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FaceitTeamTextResponseParams = TypedDict('FaceitTeamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FaceitTeamStreamParams = TypedDict('FaceitTeamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FaceitTournamentsPastDefaultParams = TypedDict('FaceitTournamentsPastDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'nickname': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitTournamentsPastTextResponseParams = TypedDict('FaceitTournamentsPastTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'nickname': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitTournamentsPastStreamParams = TypedDict('FaceitTournamentsPastStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'nickname': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

FaceitUserSkillsDefaultParams = TypedDict('FaceitUserSkillsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_ids': Required[list[str]],
    'game': Required[str],
}, total=False)

FaceitUserSkillsTextResponseParams = TypedDict('FaceitUserSkillsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_ids': Required[list[str]],
    'game': Required[str],
}, total=False)

FaceitUserSkillsStreamParams = TypedDict('FaceitUserSkillsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_ids': Required[list[str]],
    'game': Required[str],
}, total=False)
