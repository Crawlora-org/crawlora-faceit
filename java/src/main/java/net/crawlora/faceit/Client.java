package net.crawlora.faceit;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the FACEIT endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 35;
    public static final List<String> OPERATION_IDS = List.of(
            "faceit-ban-reasons",
            "faceit-banlist",
            "faceit-banlist-stats",
            "faceit-best-clips",
            "faceit-championship",
            "faceit-championship-bracket",
            "faceit-championship-participants",
            "faceit-championship-search",
            "faceit-clip",
            "faceit-clips",
            "faceit-competition-matches",
            "faceit-fpl",
            "faceit-game-modes",
            "faceit-games",
            "faceit-hub",
            "faceit-hub-categories",
            "faceit-hub-memberships",
            "faceit-hubs",
            "faceit-hubs-detailed",
            "faceit-leaderboard",
            "faceit-leaderboard-detail",
            "faceit-leaderboard-statuses",
            "faceit-maps",
            "faceit-match-clips",
            "faceit-organizer",
            "faceit-player",
            "faceit-player-rank",
            "faceit-regions",
            "faceit-rule",
            "faceit-rules",
            "faceit-skill-levels",
            "faceit-standings",
            "faceit-team",
            "faceit-tournaments-past",
            "faceit-user-skills"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("faceit-ban-reasons", new Operation("faceit-ban-reasons", "GET", "/faceit/ban-reasons", Map.of(), List.of("application/json")));
        operations.put("faceit-banlist", new Operation("faceit-banlist", "GET", "/faceit/banlist", Map.ofEntries(Map.entry("size", new Param("size", "query", false, "integer", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "string", List.of(), "csv")), Map.entry("reason", new Param("reason", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-banlist-stats", new Operation("faceit-banlist-stats", "GET", "/faceit/banlist-stats", Map.of(), List.of("application/json")));
        operations.put("faceit-best-clips", new Operation("faceit-best-clips", "GET", "/faceit/best-clips", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("cs2"), "csv")), Map.entry("user_id", new Param("user_id", "query", true, "string", List.of(), "csv")), Map.entry("from", new Param("from", "query", true, "string", List.of(), "csv")), Map.entry("to", new Param("to", "query", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-championship", new Operation("faceit-championship", "GET", "/faceit/championship", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-championship-bracket", new Operation("faceit-championship-bracket", "GET", "/faceit/championship-bracket", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("group", new Param("group", "query", true, "integer", List.of(), "csv")), Map.entry("round", new Param("round", "query", true, "integer", List.of(), "csv")), Map.entry("start", new Param("start", "query", false, "integer", List.of(), "csv")), Map.entry("end", new Param("end", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-championship-participants", new Operation("faceit-championship-participants", "GET", "/faceit/championship-participants", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-championship-search", new Operation("faceit-championship-search", "GET", "/faceit/championship-search", Map.ofEntries(Map.entry("entity_type", new Param("entity_type", "query", false, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of(), "csv")), Map.entry("status", new Param("status", "query", false, "string", List.of("ONGOING", "UPCOMING", "FINISHED"), "csv")), Map.entry("subtype", new Param("subtype", "query", false, "string", List.of(), "csv")), Map.entry("country", new Param("country", "query", false, "string", List.of(), "csv")), Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"), "csv")), Map.entry("has_drops", new Param("has_drops", "query", false, "boolean", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-clip", new Operation("faceit-clip", "GET", "/faceit/clip", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-clips", new Operation("faceit-clips", "GET", "/faceit/clips", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("cs2"), "csv")), Map.entry("user_id", new Param("user_id", "query", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-competition-matches", new Operation("faceit-competition-matches", "GET", "/faceit/competition-matches", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", true, "string", List.of(), "csv")), Map.entry("player_id", new Param("player_id", "query", false, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("size", new Param("size", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-fpl", new Operation("faceit-fpl", "GET", "/faceit/fpl", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of("cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-game-modes", new Operation("faceit-game-modes", "GET", "/faceit/game-modes", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"), "csv")), Map.entry("region", new Param("region", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-games", new Operation("faceit-games", "GET", "/faceit/games", Map.of(), List.of("application/json")));
        operations.put("faceit-hub", new Operation("faceit-hub", "GET", "/faceit/hub", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-hub-categories", new Operation("faceit-hub-categories", "GET", "/faceit/hub-categories", Map.of(), List.of("application/json")));
        operations.put("faceit-hub-memberships", new Operation("faceit-hub-memberships", "GET", "/faceit/hub-memberships", Map.ofEntries(Map.entry("user_id", new Param("user_id", "query", true, "string", List.of(), "csv")), Map.entry("category", new Param("category", "query", false, "string", List.of("community", "chat", "ihl"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-hubs", new Operation("faceit-hubs", "GET", "/faceit/hubs", Map.ofEntries(Map.entry("ids", new Param("ids", "query", true, "array", List.of(), "multi"))), List.of("application/json")));
        operations.put("faceit-hubs-detailed", new Operation("faceit-hubs-detailed", "GET", "/faceit/hubs-detailed", Map.ofEntries(Map.entry("ids", new Param("ids", "query", true, "array", List.of(), "multi"))), List.of("application/json")));
        operations.put("faceit-leaderboard", new Operation("faceit-leaderboard", "GET", "/faceit/leaderboard", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"), "csv")), Map.entry("region", new Param("region", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-leaderboard-detail", new Operation("faceit-leaderboard-detail", "GET", "/faceit/leaderboard-detail", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-leaderboard-statuses", new Operation("faceit-leaderboard-statuses", "GET", "/faceit/leaderboard-statuses", Map.of(), List.of("application/json")));
        operations.put("faceit-maps", new Operation("faceit-maps", "GET", "/faceit/maps", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"), "csv"))), List.of("application/json")));
        operations.put("faceit-match-clips", new Operation("faceit-match-clips", "GET", "/faceit/match-clips", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("cs2"), "csv")), Map.entry("match_id", new Param("match_id", "query", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-organizer", new Operation("faceit-organizer", "GET", "/faceit/organizer", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-player", new Operation("faceit-player", "GET", "/faceit/player", Map.ofEntries(Map.entry("nickname", new Param("nickname", "query", false, "string", List.of(), "csv")), Map.entry("user_id", new Param("user_id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-player-rank", new Operation("faceit-player-rank", "GET", "/faceit/player-rank", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"), "csv")), Map.entry("region", new Param("region", "query", true, "string", List.of(), "csv")), Map.entry("nickname", new Param("nickname", "query", false, "string", List.of(), "csv")), Map.entry("user_id", new Param("user_id", "query", false, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-regions", new Operation("faceit-regions", "GET", "/faceit/regions", Map.of(), List.of("application/json")));
        operations.put("faceit-rule", new Operation("faceit-rule", "GET", "/faceit/rule", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-rules", new Operation("faceit-rules", "GET", "/faceit/rules", Map.ofEntries(Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-skill-levels", new Operation("faceit-skill-levels", "GET", "/faceit/skill-levels", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("cs2", "csgo", "ow2", "valorant", "pubg", "tf2", "krunker", "pubgmobile", "apex", "fortnite", "wow", "brawl_stars", "insidia", "dota2", "hearthstone", "wildrift", "clash_royale", "smite", "lol_NA", "lol_EUW", "lol_EUN", "overwatch_EU", "wot_EU", "wot_RU", "rainbow_6", "csdz", "battalion"), "csv"))), List.of("application/json")));
        operations.put("faceit-standings", new Operation("faceit-standings", "GET", "/faceit/standings", Map.ofEntries(Map.entry("entity_id", new Param("entity_id", "query", true, "string", List.of(), "csv")), Map.entry("group", new Param("group", "query", true, "integer", List.of(), "csv")), Map.entry("round", new Param("round", "query", true, "string", List.of(), "csv")), Map.entry("segment", new Param("segment", "query", false, "integer", List.of(), "csv")), Map.entry("match", new Param("match", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-team", new Operation("faceit-team", "GET", "/faceit/team", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-tournaments-past", new Operation("faceit-tournaments-past", "GET", "/faceit/tournaments-past", Map.ofEntries(Map.entry("nickname", new Param("nickname", "query", true, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("faceit-user-skills", new Operation("faceit-user-skills", "GET", "/faceit/user-skills", Map.ofEntries(Map.entry("user_ids", new Param("user_ids", "query", true, "array", List.of(), "multi")), Map.entry("game", new Param("game", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown FACEIT operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object banReasons(Map<String, ?> params) { return request("faceit-ban-reasons", params); }
    public Object banlist(Map<String, ?> params) { return request("faceit-banlist", params); }
    public Object banlistStats(Map<String, ?> params) { return request("faceit-banlist-stats", params); }
    public Object bestClips(Map<String, ?> params) { return request("faceit-best-clips", params); }
    public Object championship(Map<String, ?> params) { return request("faceit-championship", params); }
    public Object championshipBracket(Map<String, ?> params) { return request("faceit-championship-bracket", params); }
    public Object championshipParticipants(Map<String, ?> params) { return request("faceit-championship-participants", params); }
    public Object championshipSearch(Map<String, ?> params) { return request("faceit-championship-search", params); }
    public Object clip(Map<String, ?> params) { return request("faceit-clip", params); }
    public Object clips(Map<String, ?> params) { return request("faceit-clips", params); }
    public Object competitionMatches(Map<String, ?> params) { return request("faceit-competition-matches", params); }
    public Object fpl(Map<String, ?> params) { return request("faceit-fpl", params); }
    public Object gameModes(Map<String, ?> params) { return request("faceit-game-modes", params); }
    public Object games(Map<String, ?> params) { return request("faceit-games", params); }
    public Object hub(Map<String, ?> params) { return request("faceit-hub", params); }
    public Object hubCategories(Map<String, ?> params) { return request("faceit-hub-categories", params); }
    public Object hubMemberships(Map<String, ?> params) { return request("faceit-hub-memberships", params); }
    public Object hubs(Map<String, ?> params) { return request("faceit-hubs", params); }
    public Object hubsDetailed(Map<String, ?> params) { return request("faceit-hubs-detailed", params); }
    public Object leaderboard(Map<String, ?> params) { return request("faceit-leaderboard", params); }
    public Object leaderboardDetail(Map<String, ?> params) { return request("faceit-leaderboard-detail", params); }
    public Object leaderboardStatuses(Map<String, ?> params) { return request("faceit-leaderboard-statuses", params); }
    public Object maps(Map<String, ?> params) { return request("faceit-maps", params); }
    public Object matchClips(Map<String, ?> params) { return request("faceit-match-clips", params); }
    public Object organizer(Map<String, ?> params) { return request("faceit-organizer", params); }
    public Object player(Map<String, ?> params) { return request("faceit-player", params); }
    public Object playerRank(Map<String, ?> params) { return request("faceit-player-rank", params); }
    public Object regions(Map<String, ?> params) { return request("faceit-regions", params); }
    public Object rule(Map<String, ?> params) { return request("faceit-rule", params); }
    public Object rules(Map<String, ?> params) { return request("faceit-rules", params); }
    public Object skillLevels(Map<String, ?> params) { return request("faceit-skill-levels", params); }
    public Object standings(Map<String, ?> params) { return request("faceit-standings", params); }
    public Object team(Map<String, ?> params) { return request("faceit-team", params); }
    public Object tournamentsPast(Map<String, ?> params) { return request("faceit-tournaments-past", params); }
    public Object userSkills(Map<String, ?> params) { return request("faceit-user-skills", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
