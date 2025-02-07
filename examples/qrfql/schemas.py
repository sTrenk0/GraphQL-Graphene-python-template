from graphene import Schema
from .services.queries import Query
from .services.mutations import Mutation


# Different schemes that encapsulate the entire graphQL logic.
schema = Schema(query=Query, mutation=Mutation)
