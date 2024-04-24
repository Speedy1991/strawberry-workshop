from django.conf import settings
from django.views.generic import RedirectView

from final.schema.schema import schema
from django.urls import path
from strawberry.django.views import GraphQLView

urlpatterns = [
    path('', RedirectView.as_view(url='graphql/', permanent=False)),
    path('graphql/', GraphQLView.as_view(
        schema=schema,
        graphql_ide=settings.STRAWBERRY_GRAPHQL_IDE,
    ))
]
