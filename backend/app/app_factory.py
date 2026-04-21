from fastapi import FastAPI

from apps.info.router import info_router


def get_application() -> FastAPI:
    app = FastAPI()

    app.include_router(info_router, tags=["User"])

    return app
