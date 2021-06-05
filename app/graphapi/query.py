import strawberry as stb
from app.crud import cruduser
from app.db import get_session


@stb.type
class Query:
    @stb.field
    async def ReadUser(self, info, username: str):
        ses = await get_session()
        fields = info.field_nodes[0].selection_set.selections[0]
        return await cruduser.get_user(ses, username, fields)
