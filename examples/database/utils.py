from sqlalchemy.orm import Query, load_only, DeclarativeBase
from typing import Type


def add_specified_fields_to_query(query: Query, requested_fields: tuple, model: Type[DeclarativeBase]) -> Query:
    """
    Function that accepts the requested fields and configure the query to load
    only the specified fields based on the requested fields.
    """
    orm_fields = [getattr(model, field) for field in requested_fields if hasattr(model, field)]
    return query.options(load_only(*orm_fields))
