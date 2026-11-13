import { FaceitClient } from "../src/index.js";

const client = new FaceitClient({ apiKey: "test-key" });
void client.bestClips({"game": "cs2", "user_id": "sample", "from": "sample", "to": "sample"});
void client.request("faceit-best-clips", {"game": "cs2", "user_id": "sample", "from": "sample", "to": "sample"});
const streamResponse: Promise<Response> = client.request("faceit-best-clips", {"game": "cs2", "user_id": "sample", "from": "sample", "to": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("faceit-best-clips", {"game": "cs2", "user_id": "sample", "from": "sample", "to": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.bestClips({"game": "cs2", "user_id": "sample", "from": "sample", "to": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("faceit-best-clips", {"game": "cs2", "user_id": "sample", "from": "sample", "to": "sample", "limit": 1}, { responseType: "text" });
const rawText: Promise<string> = client.request("faceit-best-clips", {"game": "cs2", "user_id": "sample", "from": "sample", "to": "sample"}, { responseType: "text" });
void rawText;


void client.banReasons();
void client.request("faceit-ban-reasons");
// @ts-expect-error The selected operation requires its documented params.
void client.bestClips();
