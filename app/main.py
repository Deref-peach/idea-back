from app.graphapi import schema
from starlette.applications import Starlette
from app.core.config import settings
from strawberry.asgi import GraphQL
import uvicorn
from app.restapi import middlewares, routes


app = Starlette(debug=settings.DEBUG, routes=routes, middleware=middlewares)

graphql_app = GraphQL(schema, debug=settings.DEBUG)

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

if __name__ == '__main__':
    uvicorn.run(app, loop="none", host='127.0.0.1', port=settings.PORT, log_level="error")
