from typing import Any

from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from strawberry.django.views import AsyncGraphQLView

from core.dataloaders import inject_dataloaders


@method_decorator(ensure_csrf_cookie, 'dispatch')
class PatchedGraphQLView(AsyncGraphQLView):
    async def get_context(self, request, response) -> Any:
        ctx = await super().get_context(request, response)
        inject_dataloaders(ctx)
        return ctx

    def is_request_allowed(self, request: HttpRequest) -> bool:
        if self.graphql_ide:
            return request.method.lower() in ('get', 'post')
        return request.method.lower() == 'post'
