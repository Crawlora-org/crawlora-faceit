import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class FaceitClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-faceit-js/0.1.0" });
    this["banReasons"] = (...args) => this.request("faceit-ban-reasons", ...args);
    this["banlist"] = (...args) => this.request("faceit-banlist", ...args);
    this["banlistStats"] = (...args) => this.request("faceit-banlist-stats", ...args);
    this["bestClips"] = (...args) => this.request("faceit-best-clips", ...args);
    this["championship"] = (...args) => this.request("faceit-championship", ...args);
    this["championshipBracket"] = (...args) => this.request("faceit-championship-bracket", ...args);
    this["championshipParticipants"] = (...args) => this.request("faceit-championship-participants", ...args);
    this["championshipSearch"] = (...args) => this.request("faceit-championship-search", ...args);
    this["clip"] = (...args) => this.request("faceit-clip", ...args);
    this["clips"] = (...args) => this.request("faceit-clips", ...args);
    this["competitionMatches"] = (...args) => this.request("faceit-competition-matches", ...args);
    this["fpl"] = (...args) => this.request("faceit-fpl", ...args);
    this["gameModes"] = (...args) => this.request("faceit-game-modes", ...args);
    this["games"] = (...args) => this.request("faceit-games", ...args);
    this["hub"] = (...args) => this.request("faceit-hub", ...args);
    this["hubCategories"] = (...args) => this.request("faceit-hub-categories", ...args);
    this["hubMemberships"] = (...args) => this.request("faceit-hub-memberships", ...args);
    this["hubs"] = (...args) => this.request("faceit-hubs", ...args);
    this["hubsDetailed"] = (...args) => this.request("faceit-hubs-detailed", ...args);
    this["leaderboard"] = (...args) => this.request("faceit-leaderboard", ...args);
    this["leaderboardDetail"] = (...args) => this.request("faceit-leaderboard-detail", ...args);
    this["leaderboardStatuses"] = (...args) => this.request("faceit-leaderboard-statuses", ...args);
    this["maps"] = (...args) => this.request("faceit-maps", ...args);
    this["matchClips"] = (...args) => this.request("faceit-match-clips", ...args);
    this["organizer"] = (...args) => this.request("faceit-organizer", ...args);
    this["player"] = (...args) => this.request("faceit-player", ...args);
    this["playerRank"] = (...args) => this.request("faceit-player-rank", ...args);
    this["regions"] = (...args) => this.request("faceit-regions", ...args);
    this["rule"] = (...args) => this.request("faceit-rule", ...args);
    this["rules"] = (...args) => this.request("faceit-rules", ...args);
    this["skillLevels"] = (...args) => this.request("faceit-skill-levels", ...args);
    this["standings"] = (...args) => this.request("faceit-standings", ...args);
    this["team"] = (...args) => this.request("faceit-team", ...args);
    this["tournamentsPast"] = (...args) => this.request("faceit-tournaments-past", ...args);
    this["userSkills"] = (...args) => this.request("faceit-user-skills", ...args);
  }
}

export { FaceitClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default FaceitClient;
