from fastapi import FastAPI
from qrfql.schemas import schema
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

app = FastAPI(description="GraphQL API")
app.mount("/graphql", GraphQLApp(schema=schema, on_get=make_graphiql_handler()))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
