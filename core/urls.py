from django.conf import settings
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import RedirectView

from core.views.app_entry_view import AppEntryPoint
from core.views.graphql_view import PatchedGraphQLView
from core.views.graphql_ws import websocket_view
from final.schema.schema import schema

urlpatterns = [
    path('', RedirectView.as_view(url='graphql/', permanent=False)),
    path('graphql/', PatchedGraphQLView.as_view(
        schema=schema,
        graphql_ide='apollo-sandbox',
        multipart_uploads_enabled=True
    )),
    path('graphqlws/', websocket_view(schema=schema)),
    path('app/', AppEntryPoint.as_view())
]


if settings.DEBUG:
    urlpatterns += [
        path('graphql_no_csrf/', csrf_exempt(PatchedGraphQLView.as_view(
            schema=schema,
            graphql_ide='apollo-sandbox',
        ))),
    ]