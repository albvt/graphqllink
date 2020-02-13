import graphene
import graphene
import graphql_jwt

import graphqllinks.schema
import users.schema
import graphqllinks.schema_relay




# Add the users.schema.Query
##we have a query and mutation
class Query(
    graphqllinks.schema_relay.RelayQuery,
    users.schema.Query,
    graphqllinks.schema.Query,
    graphene.ObjectType):
    pass

class Mutation(
    users.schema.Mutation,
    graphqllinks.schema.Mutation,
    graphqllinks.schema_relay.RelayMutation,
    graphene.ObjectType):

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
