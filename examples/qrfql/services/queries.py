from typing import Optional

from graphene import ObjectType, Int, List, Field

from database.models import UserModel
from database.services import user_dal_service
from ..types import UserType
from ..utils import get_requested_fields


class UserQueries:
    """This class contains queries for fetching user data."""

    users = List(UserType)
    user_by_id = Field(UserType, id=Int())

    def resolve_users(self, info) -> list[Optional[UserModel]]:
        requested_fields = get_requested_fields(info)
        return user_dal_service.get_all(requested_fields)

    def resolve_user_by_id(self, info, id) -> Optional[UserModel]:
        requested_fields = get_requested_fields(info)
        return user_dal_service.get_by_id(id, requested_fields)


class Query(UserQueries, ObjectType):
    """
    Main query class containing all queries.
    Can be extended to include additional queries.
    """
    pass
