import graphene


class Query(
    # add your multiple schemas from yours apps
    # example.schema.Queries,
    graphene.ObjectType
):
    hello = graphene.String(default_value="Hi!")
    pass


class Mutation(
    # add your multiple mutations from yours apps
    # example.schema.Mutations,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(
    query=Query,
    # mutation=Mutation
)
