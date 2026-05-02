from typing import Optional

from fastapi import Header
from settings import settings


async def language_header(
    accept_language: Optional[str] = Header(
        settings.DEFAULT_LANGUAGE,
        description="Optional language override",
        alias=settings.LANGUAGE_HEADER,
    ),
) -> str:
    return accept_language
