"""Typed FACEIT client for the Crawlora hosted API."""

from .platform import FaceitClient, AsyncFaceitClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = FaceitClient
AsyncClient = AsyncFaceitClient
__version__ = '0.1.0'
DISPLAY_NAME = 'FACEIT'
PLATFORM = 'faceit'
CONTRACT_REVISION = 'sha256:d14c7026f59aa4e03ae84775c08493086732dd9c06000fca9bb721c3772e03cb'

__all__ = [
    "FaceitClient", "AsyncFaceitClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
