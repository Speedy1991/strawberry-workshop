"""
ASGI config for strawberry_workshop project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django

from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler
from django.core.handlers.asgi import ASGIHandler
from django.urls import resolve
from starlette.responses import PlainTextResponse
from starlette.websockets import WebSocket


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'strawberry_workshop.settings')

def get_application():
    django.setup()
    # HINT: Yea we serve ASGIStaticFiles, in a prod environment a reverse proxy should be used leading to /static will never hit the django server in prod
    return ASGIStaticFilesHandler(ASGIHandler())

# HINT: This is very raw code for max performance and highest adaptability
# HINT: This will also work with a starlette Router and use Django as a middleware application
# HINT: DO NOT USE THIS IN PRODUCTION - there is not a single rate limiting implemented -> DDOS
# DOCS: Example ratelimiter: https://django-ratelimit.readthedocs.io/en/stable/
# HINT: You should really know what you do if you mess with the asgi handler yourself :)
def router(app):
    async def asgi(scope, receive, send):
        if scope["type"] == "websocket":
            # Handle websockets with starlette but in a django context? No Problem!
            # The matched function _must_ be implemented in django. e.g. as /graphql_ws Route. Inside this route you can handle your subscriptions :)
            match = resolve(scope["raw_path"].decode("ascii"))
            # Care you are responsible to create the request stuff and security yourself. The django middlewarestack IS NOT APPLIED!!!
            # https://strawberry.rocks/docs/integrations/starlette
            await match.func(WebSocket(scope, receive, send), *match.args, **match.kwargs)
            return

        raw_path = scope.get('path', None)
        if scope["type"] == "http":
            if raw_path == '/test/':
                await PlainTextResponse('Hello from test - no django code is executed')(scope, receive, send)
                return
        try:
            await app(scope, receive, send)
        except Exception as e:
            # Todo some custom error handling?
            raise e
    return asgi


application = router(get_application())
