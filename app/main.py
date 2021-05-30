from fastapi import FastAPI
from app.core import settings
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import apirouter as api_v1
from app.api.v1.graphql.schema import schema
from starlette.graphql import GraphQLApp
from strawberry.asgi import GraphQL

app = FastAPI(debug=settings.DEBUG, title=settings.TITLE, )

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_v1, prefix='/api/v1/')
app.add_route('/api/v1/graphql', GraphQL(schema))
