from typing import Callable

from fastapi import Request


async def get_gettext(request: Request) -> Callable:
    _ = getattr(request.state, "_", lambda x: x)
    return _
