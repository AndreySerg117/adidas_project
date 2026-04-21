from fastapi import APIRouter
import socket

info_router = APIRouter()


@info_router.get("/backend")
async def get_backend_info():
    return {"backend": socket.gethostname()}