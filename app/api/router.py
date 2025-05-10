from strawberry.fastapi import GraphQLRouter

from app.api.schema import schema


graphql_router = GraphQLRouter(schema, allow_queries_via_get=False)
