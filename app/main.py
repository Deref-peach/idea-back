from app.graphapi import schema
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from app.core.config import settings
from strawberry.asgi import GraphQL
import uvicorn
from app.restapi import routes


app = Starlette(debug=settings.DEBUG, routes=routes)
app.add_middleware(
    CORSMiddleware, 
    allow_headers=["*"], 
    allow_origins=settings.ALLOWED_HOSTS, 
    allow_methods=["*"],
    allow_credentials=True,
)

graphql_app = GraphQL(schema, debug=settings.DEBUG)

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

if __name__ == '__main__':
    uvicorn.run(app, loop="none", host='127.0.0.1', port=settings.PORT, log_level="error")
