import os

from crawlora_faceit import FaceitClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with FaceitClient(api_key=api_key) as client:
    games = client.games()
    print('games', games)
    banlist_stats = client.banlist_stats()
    print('banlist_stats', banlist_stats)
