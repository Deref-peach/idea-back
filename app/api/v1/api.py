from fastapi import APIRouter
from .endpoints import auth

apirouter = APIRouter()

apirouter.include_router(auth.router, prefix='/')
