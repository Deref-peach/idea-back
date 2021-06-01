import strawberry as stb

@stb.type
class Query:
    me: list
    username: list


schema = stb.Schema(query=Query)
