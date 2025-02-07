try:
    from graphql.type import GraphQLResolveInfo as Info
    sys_version = ">=3"
except ImportError:
    from graphql import ResolveInfo as Info
    sys_version = "<3"


def get_requested_fields(info: Info) -> tuple:
    """
    Function that parses requested fields from a query.
    Сan be used in conjunction with the implementation of data loading from the database.
    """
    if sys_version == "<3":
        return tuple(field.name.value for field in info.field_asts[0].selection_set.selections)
    elif sys_version == ">=3":
        return tuple(field.name.value for field in info.field_nodes[0].selection_set.selections)


class InitMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
