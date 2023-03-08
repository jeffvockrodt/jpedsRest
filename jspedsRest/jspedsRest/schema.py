
from graphene import Schema, ObjectType
import jspeds.schema.schema
import users.gql.schema.schema


class Query(jspeds.schema.schema.Query, users.gql.schema.schema.Query, ObjectType):
  pass

class Mutation(users.gql.schema.schema.Mutation, ObjectType):
  pass

schema = Schema(query=Query, mutation=Mutation)