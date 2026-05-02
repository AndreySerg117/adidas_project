from gettext import translation
from pathlib import Path

from settings import settings
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class I18nMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        print(request.__dict__)
        print(str(Path(__file__).parent.parent / "locale"), 55555555555555555555555555)
        raw_lang = request.headers.get(
            settings.LANGUAGE_HEADER.lower(), settings.DEFAULT_LANGUAGE
        ).lower()
        if raw_lang not in settings.SUPPORTED_LANGUAGES:
            raw_lang = settings.DEFAULT_LANGUAGE

        translator = translation(
            domain="this_project",
            localedir=str(Path(__file__).parent.parent / "locale"),
            languages=[raw_lang],
            fallback=True,
        )

        request.state._ = translator.gettext

        response = await call_next(request)

        return response