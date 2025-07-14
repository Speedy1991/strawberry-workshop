import importlib

from django.conf import settings
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from core.views.app_entry_view import AppEntryPoint
from core.views.graphql_view import PatchedGraphQLView, AsyncPatchedGraphQLView
from core.views.graphql_ws import websocket_view

module = importlib.import_module(f"{settings.CURRENT_EXERCISE}.schema.schema")

view_mapper = {f"exercise{no}": PatchedGraphQLView for no in range(1, 6)}
GraphQLView = view_mapper.get(settings.CURRENT_EXERCISE, AsyncPatchedGraphQLView)
schema = getattr(module, "schema")

print("Loaded module", str(module))
print("Loaded GraphQLView:", str(GraphQLView))

urlpatterns = [
    path(
        "graphql/",
        GraphQLView.as_view(
            schema=schema, graphql_ide=None, multipart_uploads_enabled=True
        ),
    ),
    path("graphqlws/", websocket_view(schema=schema)),
    re_path(r"^app/", AppEntryPoint.as_view()),
]


if settings.DEBUG:
    urlpatterns += [
        path(
            "graphiql/",
            csrf_exempt(
                GraphQLView.as_view(
                    schema=schema,
                    multipart_uploads_enabled=True,
                )
            ),
        ),
    ]
