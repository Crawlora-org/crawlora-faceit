import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class FaceitClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  banReasons(params?: OperationParamsMap["faceit-ban-reasons"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  banlist(params?: OperationParamsMap["faceit-banlist"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  banlistStats(params?: OperationParamsMap["faceit-banlist-stats"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  bestClips(params: OperationParamsMap["faceit-best-clips"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  championship(params: OperationParamsMap["faceit-championship"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  championshipBracket(params: OperationParamsMap["faceit-championship-bracket"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  championshipParticipants(params: OperationParamsMap["faceit-championship-participants"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  championshipSearch(params?: OperationParamsMap["faceit-championship-search"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  clip(params: OperationParamsMap["faceit-clip"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  clips(params: OperationParamsMap["faceit-clips"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  competitionMatches(params: OperationParamsMap["faceit-competition-matches"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  fpl(params?: OperationParamsMap["faceit-fpl"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  gameModes(params: OperationParamsMap["faceit-game-modes"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  games(params?: OperationParamsMap["faceit-games"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  hub(params: OperationParamsMap["faceit-hub"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  hubCategories(params?: OperationParamsMap["faceit-hub-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  hubMemberships(params: OperationParamsMap["faceit-hub-memberships"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  hubs(params: OperationParamsMap["faceit-hubs"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  hubsDetailed(params: OperationParamsMap["faceit-hubs-detailed"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  leaderboard(params: OperationParamsMap["faceit-leaderboard"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  leaderboardDetail(params: OperationParamsMap["faceit-leaderboard-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  leaderboardStatuses(params?: OperationParamsMap["faceit-leaderboard-statuses"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  maps(params: OperationParamsMap["faceit-maps"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchClips(params: OperationParamsMap["faceit-match-clips"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  organizer(params: OperationParamsMap["faceit-organizer"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  player(params?: OperationParamsMap["faceit-player"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerRank(params: OperationParamsMap["faceit-player-rank"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  regions(params?: OperationParamsMap["faceit-regions"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  rule(params: OperationParamsMap["faceit-rule"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  rules(params?: OperationParamsMap["faceit-rules"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  skillLevels(params: OperationParamsMap["faceit-skill-levels"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  standings(params: OperationParamsMap["faceit-standings"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  team(params: OperationParamsMap["faceit-team"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentsPast(params: OperationParamsMap["faceit-tournaments-past"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  userSkills(params: OperationParamsMap["faceit-user-skills"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  banReasons(params?: OperationParamsMap["faceit-ban-reasons"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  banlist(params?: OperationParamsMap["faceit-banlist"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  banlistStats(params?: OperationParamsMap["faceit-banlist-stats"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  bestClips(params: OperationParamsMap["faceit-best-clips"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  championship(params: OperationParamsMap["faceit-championship"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  championshipBracket(params: OperationParamsMap["faceit-championship-bracket"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  championshipParticipants(params: OperationParamsMap["faceit-championship-participants"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  championshipSearch(params?: OperationParamsMap["faceit-championship-search"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  clip(params: OperationParamsMap["faceit-clip"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  clips(params: OperationParamsMap["faceit-clips"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  competitionMatches(params: OperationParamsMap["faceit-competition-matches"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  fpl(params?: OperationParamsMap["faceit-fpl"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  gameModes(params: OperationParamsMap["faceit-game-modes"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  games(params?: OperationParamsMap["faceit-games"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  hub(params: OperationParamsMap["faceit-hub"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  hubCategories(params?: OperationParamsMap["faceit-hub-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  hubMemberships(params: OperationParamsMap["faceit-hub-memberships"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  hubs(params: OperationParamsMap["faceit-hubs"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  hubsDetailed(params: OperationParamsMap["faceit-hubs-detailed"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  leaderboard(params: OperationParamsMap["faceit-leaderboard"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  leaderboardDetail(params: OperationParamsMap["faceit-leaderboard-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  leaderboardStatuses(params?: OperationParamsMap["faceit-leaderboard-statuses"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  maps(params: OperationParamsMap["faceit-maps"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchClips(params: OperationParamsMap["faceit-match-clips"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  organizer(params: OperationParamsMap["faceit-organizer"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  player(params?: OperationParamsMap["faceit-player"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerRank(params: OperationParamsMap["faceit-player-rank"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  regions(params?: OperationParamsMap["faceit-regions"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  rule(params: OperationParamsMap["faceit-rule"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  rules(params?: OperationParamsMap["faceit-rules"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  skillLevels(params: OperationParamsMap["faceit-skill-levels"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  standings(params: OperationParamsMap["faceit-standings"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  team(params: OperationParamsMap["faceit-team"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentsPast(params: OperationParamsMap["faceit-tournaments-past"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  userSkills(params: OperationParamsMap["faceit-user-skills"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  banReasons(...args: OperationRequestArgs<"faceit-ban-reasons">): Promise<OperationResponseMap["faceit-ban-reasons"]>;
  banlist(...args: OperationRequestArgs<"faceit-banlist">): Promise<OperationResponseMap["faceit-banlist"]>;
  banlistStats(...args: OperationRequestArgs<"faceit-banlist-stats">): Promise<OperationResponseMap["faceit-banlist-stats"]>;
  bestClips(...args: OperationRequestArgs<"faceit-best-clips">): Promise<OperationResponseMap["faceit-best-clips"]>;
  championship(...args: OperationRequestArgs<"faceit-championship">): Promise<OperationResponseMap["faceit-championship"]>;
  championshipBracket(...args: OperationRequestArgs<"faceit-championship-bracket">): Promise<OperationResponseMap["faceit-championship-bracket"]>;
  championshipParticipants(...args: OperationRequestArgs<"faceit-championship-participants">): Promise<OperationResponseMap["faceit-championship-participants"]>;
  championshipSearch(...args: OperationRequestArgs<"faceit-championship-search">): Promise<OperationResponseMap["faceit-championship-search"]>;
  clip(...args: OperationRequestArgs<"faceit-clip">): Promise<OperationResponseMap["faceit-clip"]>;
  clips(...args: OperationRequestArgs<"faceit-clips">): Promise<OperationResponseMap["faceit-clips"]>;
  competitionMatches(...args: OperationRequestArgs<"faceit-competition-matches">): Promise<OperationResponseMap["faceit-competition-matches"]>;
  fpl(...args: OperationRequestArgs<"faceit-fpl">): Promise<OperationResponseMap["faceit-fpl"]>;
  gameModes(...args: OperationRequestArgs<"faceit-game-modes">): Promise<OperationResponseMap["faceit-game-modes"]>;
  games(...args: OperationRequestArgs<"faceit-games">): Promise<OperationResponseMap["faceit-games"]>;
  hub(...args: OperationRequestArgs<"faceit-hub">): Promise<OperationResponseMap["faceit-hub"]>;
  hubCategories(...args: OperationRequestArgs<"faceit-hub-categories">): Promise<OperationResponseMap["faceit-hub-categories"]>;
  hubMemberships(...args: OperationRequestArgs<"faceit-hub-memberships">): Promise<OperationResponseMap["faceit-hub-memberships"]>;
  hubs(...args: OperationRequestArgs<"faceit-hubs">): Promise<OperationResponseMap["faceit-hubs"]>;
  hubsDetailed(...args: OperationRequestArgs<"faceit-hubs-detailed">): Promise<OperationResponseMap["faceit-hubs-detailed"]>;
  leaderboard(...args: OperationRequestArgs<"faceit-leaderboard">): Promise<OperationResponseMap["faceit-leaderboard"]>;
  leaderboardDetail(...args: OperationRequestArgs<"faceit-leaderboard-detail">): Promise<OperationResponseMap["faceit-leaderboard-detail"]>;
  leaderboardStatuses(...args: OperationRequestArgs<"faceit-leaderboard-statuses">): Promise<OperationResponseMap["faceit-leaderboard-statuses"]>;
  maps(...args: OperationRequestArgs<"faceit-maps">): Promise<OperationResponseMap["faceit-maps"]>;
  matchClips(...args: OperationRequestArgs<"faceit-match-clips">): Promise<OperationResponseMap["faceit-match-clips"]>;
  organizer(...args: OperationRequestArgs<"faceit-organizer">): Promise<OperationResponseMap["faceit-organizer"]>;
  player(...args: OperationRequestArgs<"faceit-player">): Promise<OperationResponseMap["faceit-player"]>;
  playerRank(...args: OperationRequestArgs<"faceit-player-rank">): Promise<OperationResponseMap["faceit-player-rank"]>;
  regions(...args: OperationRequestArgs<"faceit-regions">): Promise<OperationResponseMap["faceit-regions"]>;
  rule(...args: OperationRequestArgs<"faceit-rule">): Promise<OperationResponseMap["faceit-rule"]>;
  rules(...args: OperationRequestArgs<"faceit-rules">): Promise<OperationResponseMap["faceit-rules"]>;
  skillLevels(...args: OperationRequestArgs<"faceit-skill-levels">): Promise<OperationResponseMap["faceit-skill-levels"]>;
  standings(...args: OperationRequestArgs<"faceit-standings">): Promise<OperationResponseMap["faceit-standings"]>;
  team(...args: OperationRequestArgs<"faceit-team">): Promise<OperationResponseMap["faceit-team"]>;
  tournamentsPast(...args: OperationRequestArgs<"faceit-tournaments-past">): Promise<OperationResponseMap["faceit-tournaments-past"]>;
  userSkills(...args: OperationRequestArgs<"faceit-user-skills">): Promise<OperationResponseMap["faceit-user-skills"]>;
}
export { FaceitClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default FaceitClient;
