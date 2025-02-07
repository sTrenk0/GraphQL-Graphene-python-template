from typing import Optional, Union

from graphene import Mutation, ObjectType, String, Int, Field
from sqlalchemy.exc import IntegrityError

from ..types import UserType
from database.models import UserModel
from database.services import user_dal_service


class CreateUser(Mutation):
    class Arguments:
        password = String(required=True)
        name = String(required=True)
        age = Int(required=True)

    user = Field(UserType)  # Response field

    def mutate(self, info, name, age, password) -> "CreateUser":
        """Handles user creation."""
        try:
            user = user_dal_service.create(UserModel(name=name, age=age, password=password))
        except IntegrityError:
            raise Exception("Failed to create user")

        return CreateUser(user=UserType(name=name, age=age, id=user.id))


class UpdateUser(Mutation):
    class Arguments:
        id = Int(required=True)
        password = String(required=False)
        name = String(required=False)
        age = Int(required=False)

    user = Field(UserType)  # Response field

    def mutate(
            self, info, id: int,
            password: Optional[str] = None,
            name: Optional[str] = None,
            age: Optional[int] = None
    ) -> Union["UpdateUser", None]:
        """Handles user updates."""
        user = user_dal_service.get_by_id(id)
        if user:
            data_to_update = {
                k: v for k, v in {
                    "password": password, "name": name, "age": age
                }.items() if v is not None
            }
            if not data_to_update:
                return None

            user_dal_service.update(user, **data_to_update)
        else:
            raise Exception("Failed to update user")

        return UpdateUser(user=UserType(name=name, age=age, id=user.id))


class DeleteUser(Mutation):
    class Arguments:
        id = Int(required=True)

    user = Field(UserType)  # Response field

    def mutate(self, info, id) -> "DeleteUser":
        """Handles user deletion."""
        user = user_dal_service.get_by_id(id)
        if user:
            user_dal_service.delete(user)
        else:
            raise Exception("Failed to delete user")

        return DeleteUser(user=UserType(name=user.name, age=user.age, id=user.id))


# ObjectType containing user mutations
class UserMutations(ObjectType):
    create_user = CreateUser.Field()  # Field for user creation
    update_user = UpdateUser.Field()  # Field for user updates
    delete_user = DeleteUser.Field()  # Field for user deletion


# Main mutation class containing all mutations, which can be split into different classes like Product, etc.
class Mutation(UserMutations):
    pass
