import io

from django.core.handlers.asgi import ASGIRequest
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseForbidden, HttpResponse
from django.middleware.csrf import CsrfViewMiddleware, _check_token_format, _does_token_match, InvalidTokenFormat
from starlette.websockets import WebSocket, WebSocketDisconnect
from strawberry.asgi import GraphQL
from strawberry.django.context import StrawberryDjangoContext
from strawberry.subscriptions.protocols.graphql_transport_ws.handlers import BaseGraphQLTransportWSHandler
from strawberry.subscriptions.protocols.graphql_transport_ws.types import ConnectionInitMessage


class PatchedBaseGraphQLTransportWSHandler(BaseGraphQLTransportWSHandler):

    async def handle_connection_init(self, message: ConnectionInitMessage) -> None:
        payload = message['payload']
        request = self.context.request

        csrf_token_payload = payload['csrfToken']
        csrf_middleware = CsrfViewMiddleware(HttpResponse)
        try:
            csrf_secret = csrf_middleware._get_secret(request)
            _check_token_format(csrf_token_payload)
            if not _does_token_match(csrf_token_payload, csrf_secret):
                raise InvalidTokenFormat('CSRF token from websocket incorrect')
        except InvalidTokenFormat as e:
            await self.websocket.close(code=4401, reason=e.reason)
            return
        except Exception:
            await self.websocket.close(code=4401, reason='Failed CSRF check')
            return
        return await super().handle_connection_init(message)



class PatchedGraphQL(GraphQL):
    graphql_transport_ws_handler_class = PatchedBaseGraphQLTransportWSHandler


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
            ws = PatchedGraphQL(schema=schema, keep_alive=True, keep_alive_interval=10, debug=True)
            context = StrawberryDjangoContext(request=request, response=HttpResponse())
            try:
                await ws.run(request=socket, context=context)
            except WebSocketDisconnect:
                pass

    return _view