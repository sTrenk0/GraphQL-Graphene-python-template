from graphene import ObjectType, String, Int

from .utils import InitMixin


# The data structures that graphene understands and returns to the client
class UserType(ObjectType, InitMixin):
    id = Int()
    name = String()
    age = Int()
