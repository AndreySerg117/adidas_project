from dependencies.headers import language_header
from fastapi import Depends, FastAPI
from middlewares.i18n import I18nMiddleware

from apps.info.router import info_router


def get_application() -> FastAPI:
    app = FastAPI(dependencies=[Depends(language_header)],)
    app.add_middleware(I18nMiddleware)

    app.include_router(info_router, tags=["User"])

    return app
