from typing import Optional
import strawberry as stb
from app.schemas.user import CreateUser, DeleteUser
from app.crud import cruduser
import uuid
from app.utils import send_del_account_email, send_new_account_email
from app.db import get_session
from app.db import reg_confirm_redis, del_users_redis
from app.core.config import settings
from dataclasses import asdict


@stb.type
class UsernameAlreadyExistsError:
    username: str

@stb.type
class FieldLenError:
    pass


RegisterUserResponse = stb.union(
    "RegisterUserResponse",
    [UsernameAlreadyExistsError, FieldLenError]
)


@stb.type
class Mutation:
    @stb.mutation
    async def CreateUser(self, user: CreateUser):
        ses = get_session()
        if cruduser.username_isexist(ses, user.username):
            return UsernameAlreadyExistsError(username=user.username)
        try:
            await cruduser.create(ses, user)
        except: # len error
            return FieldLenError()
        _uuid = str(uuid.uuid4())
        link = f"/{_uuid}"
        send_new_account_email(user.email, user.username, link)

        await reg_confirm_redis.set(_uuid, user.username)
        await reg_confirm_redis.expire(_uuid, settings.REDIS_CACHE_EXP_TIME)

    @stb.mutation
    async def DeleteUser(self, user: DeleteUser):
        ses = get_session()

        _uuid = str(uuid.uuid4())
        link = f"/{_uuid}"
        send_del_account_email(user.email, user.username, link)

        await del_users_redis.set(_uuid, user.username)
        await del_users_redis.expire(_uuid, settings.REDIS_CACHE_EXP_TIME)

    @stb.mutation
    async def UpdateUser(self, user):
        pass

