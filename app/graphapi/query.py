import strawberry as stb

@stb.type
class Query:
    @stb.field
    async def ReadUser(self):
        pass
