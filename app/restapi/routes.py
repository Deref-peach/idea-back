from starlette.routing import Route
from starlette.responses import RedirectResponse
from app.db import get_session
from app.crud import cruduser
from app.crud import crudtoken


async def delete_user(request):
    ses = await get_session()
    uuid = request.path_params['uuid']
    username = crudtoken.get_username(ses, uuid)
    await cruduser.delete_by_username(ses, username)
    return RedirectResponse(url="/")

async def create_user(request):
    uuid = request.path_params['uuid']
    ses = await get_session()
    username = await crudtoken.get_username(ses, uuid)
    await cruduser.set_confirmed(ses, username)
    return RedirectResponse(url="/")


routes = [
    Route("/delete/{uuid:uuid}", delete_user),
    Route("/create/{uuid:uuid}", create_user),
]

