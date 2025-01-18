import io

from django.conf import settings
from django.core.handlers.asgi import ASGIRequest
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseForbidden, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import RedirectView
from starlette.websockets import WebSocket, WebSocketDisconnect
from strawberry.asgi import GraphQL
from strawberry.django.context import StrawberryDjangoContext

from final.schema.schema import schema
from django.urls import path
from strawberry.django.views import AsyncGraphQLView


def create_django_asgi_request_from_starlette_websocket(websocket):
    scope = websocket.scope
    http_scope = {
        "type": "http",
        "asgi": scope["asgi"],
        "http_version": "1.1",  # WebSocket uses HTTP/1.1 for the handshake
        "method": "GET",  # WebSocket handshakes use GET
        "scheme": scope.get("scheme", "ws"),
        "path": scope["path"],
        "query_string": scope["query_string"],
        "headers": scope["headers"],
        "client": scope["client"],
        "server": scope.get("server"),
    }

    asgi_request = ASGIRequest(http_scope, io.BytesIO())
    asgi_request.is_websocket = True
    asgi_request.websocket = websocket

    return asgi_request

def websocket_view(schema):
    async def _view(socket: WebSocket):

        if isinstance(socket, WSGIRequest | ASGIRequest):
            return HttpResponseForbidden()
        else:
            request = create_django_asgi_request_from_starlette_websocket(socket)
            ws = GraphQL(schema=schema, keep_alive=True, keep_alive_interval=10, debug=True)
            context = StrawberryDjangoContext(request=request, response=HttpResponse())
            try:
                await ws.run(request=socket, context=context)
            except WebSocketDisconnect:
                pass

    return _view

urlpatterns = [
    path('', RedirectView.as_view(url='graphql/', permanent=False)),
    path('graphql/', csrf_exempt(AsyncGraphQLView.as_view(
        schema=schema,
        graphql_ide='apollo-sandbox',
    ))),
    path('graphqlws/', websocket_view(schema=schema)),
]
