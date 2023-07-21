"""Module containing the implementation for the websocket to follow SansIOProtocol"""
import asyncio

from uvicorn.config import Config
from uvicorn.server import ServerState

class WebSocketSansIOProtocol(asyncio.Protocol):
    """_summary_

    Args:
        asyncio (_type_): _description_
    """
    def __init__(self, config: Config, server_state: ServerState) -> None:
        if not config.loaded:
            config.load()
        self.config = config
