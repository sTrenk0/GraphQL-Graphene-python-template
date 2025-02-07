from graphene import ObjectType, Field

from ..types import Type


class QueriesImpl:
    """This class contains queries for fetching user data."""

    query = Field(Type)

    def resolve_query(self, info):
        return None


class Query(QueriesImpl, ObjectType):
    """
    Main query class containing all queries.
    Can be extended to include additional queries.
    """
    pass
