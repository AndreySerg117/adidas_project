from fastapi import APIRouter, Depends
import socket
from services.betterstack import betterstack_log
from random import randint
import cProfile
import socket
from random import randint

from dependencies.i18n import get_gettext

info_router = APIRouter()


async def hard_calculations():
    return [{i: i ** 1} for i in range(50)]


@info_router.get("/backend")
async def get_backend_info(_=Depends(get_gettext)):
    result = {"backend": socket.gethostname(), "translated": _("Hello123"),
              "translated2": _("ldfhgjdfklhgkjdfhgkjdfhkgjdfhkg dfkjghkdfhgjhing")}
    betterstack_log.info('hello, first log', extra=result)
    betterstack_log.debug('hello, first log', extra={"debug": 44})
    return result


@info_router.get("/profile-me")
async def profile_me():
    pr = cProfile.Profile()
    pr.enable()
    await hard_calculations()
    pr.disable()
    pr.print_stats(sort="cumulative")  # Sort by cumulative time to identify bottlenecks
    betterstack_log.warning("hello, first log", extra={"no_way": randint(1, 50)})
    return {}
