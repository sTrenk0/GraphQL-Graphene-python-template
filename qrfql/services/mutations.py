from graphene import Mutation, ObjectType, String, Int, Field

from ..types import Type


class MutationImpl(Mutation):
    class Arguments:
        pass

    response_type = Field(Type)  # Response field

    def mutate(self, info, *args, **kwargs):
        return MutationImpl(response_type=Type(*args, **kwargs))


# ObjectType containing user mutations
class Mutations(ObjectType):
    mutation = MutationImpl.Field()  # Field for some mutation


# Main mutation class containing all mutations, which can be split into different classes like Product, etc.
class Mutation(Mutations):
    pass
