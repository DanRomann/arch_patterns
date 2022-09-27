from fastapi import FastAPI
from strawberry.asgi import GraphQL
from api.schema import schema


graphql_app = GraphQL(schema)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.add_route("/graphql", graphql_app)
