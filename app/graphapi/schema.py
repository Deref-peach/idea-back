import strawberry as stb
from .mutation import Mutation
from .query import Query

schema = stb.Schema(query=Query, mutation=Mutation)
