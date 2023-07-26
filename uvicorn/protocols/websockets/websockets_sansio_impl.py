"""Module containing the implementation for the websocket to follow SansIOProtocol"""
from asyncio import Protocol

from uvicorn.config import Config
from uvicorn.server import ServerState

class WebSocketSansIOProtocol(Protocol):
    """_summary_

    Args:
        asyncio (_type_): _description_
    """
    def __init__(self, config: Config, server_state: ServerState) -> None:
        if not config.loaded:
            config.load()
        self.config = config
        self.server_state = server_state
        
