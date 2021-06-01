from typing import Optional
import strawberry as stb
from app.schemas.user import CreateUser
from app.crud import cruduser

class Mutation:
    @stb.mutation
    def CreateUser(self, user: CreateUser):
        cruduser.create(user)
