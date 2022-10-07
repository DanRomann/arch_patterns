import os

from api.schema import schema
from create_db_and_fake import create_database
from fastapi import FastAPI
from models.database import DATABASE_NAME
from strawberry.asgi import GraphQL

if __name__ == "main":
    db_exist = os.path.exists(DATABASE_NAME)
    create_database(load_fake=db_exist)


graphql_app = GraphQL(schema)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.add_route("/graphql", graphql_app)
