"""Module containing the implementation for the websocket to follow SansIOProtocol"""
from asyncio import Protocol, AbstractEventLoop, get_event_loop, Transport, Queue
import logging
from typing import Dict, Any, Optional, Tuple

from uvicorn.config import Config
from uvicorn.server import ServerState


class WebSocketSansIOProtocol(Protocol):
    """_summary_

    Args:
        asyncio (_type_): _description_
    """

    def __init__(
        self,
        config: Config,
        server_state: ServerState,
        app_state: Dict[str, Any],
        _loop: Optional[AbstractEventLoop] = None,
    ) -> None:
        if not config.loaded:
            config.load()

        self.config = config
        self.app = config.loaded_app
        self.loop = _loop or get_event_loop()
        self.logger = logging.getLogger("uvicorn.debug")
        self.root_path = config.root_path
        self.app_state = app_state

        self.connections = server_state.connections
        self.tasks = server_state.tasks
        self.default_headers = server_state.default_headers

        self.transport: Transport = None  # type: ignore[assignment]
        self.server: Optional[Tuple[str, int]] = None
        self.client: Optional[Tuple[str, int]] = None
        self.scheme: Literal["wss", "ws", "wssansio"] = None  # type: ignore[assignment]

        self.queue: Queue["WebSocketEvent"] = Queue()
        self.handshake_complete = False
        self.close_sent = False