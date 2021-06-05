from typing import Optional
import strawberry as stb
from app.schemas.user import CreateUser, DeleteUser, UpdateUser
from app.crud import cruduser, crudtoken
import uuid
from app.utils import send_del_account_email, send_new_account_email
from app.db import get_session
from app.core.config import settings
from dataclasses import asdict
from app.core.security import get_password_hash

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
        ses = await get_session()
        if cruduser.username_isexist(ses, user.username):
            return UsernameAlreadyExistsError(username=user.username)
        user.hashed_password = get_password_hash(user.hashed_password)
        try:
            await cruduser.create(ses, user)
        except: # len error
            return FieldLenError()
        
        _uuid = str(uuid.uuid4())
        link = f"/{_uuid}"
        send_new_account_email(user.email, user.username, link)

        await crudtoken.create(ses, uuid=_uuid, username=user.username)

    @stb.mutation
    async def DeleteUser(self, user: DeleteUser):
        ses = await get_session()

        _uuid = str(uuid.uuid4())
        link = f"/{_uuid}"
        send_del_account_email(user.email, user.username, link)
        
        await crudtoken.create(ses, uuid=_uuid, username=user.username)

    @stb.mutation
    async def UpdateUser(self, user: UpdateUser):
        pass
