from starlette.routing import Route
from starlette.responses import RedirectResponse
from app.db import reg_confirm_redis, get_session, del_users_redis
from app.crud import cruduser

async def delete_user(request):
    uuid = request.path_params['uuid']
    val = await del_users_redis.get(uuid)
    await del_users_redis.delete(uuid)
    await cruduser.delete_by_username(get_session(), val)
    return RedirectResponse(url="/")

async def create_user(request):
    uuid = request.path_params['uuid']
    await reg_confirm_redis.delete(uuid)
    return RedirectResponse(url="/")


routes = [
    Route("/delete/{uuid:uuid}", delete_user),
    Route("/create/{uuid:uuid}", create_user),
]
