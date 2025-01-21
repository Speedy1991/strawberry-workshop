from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView


@method_decorator(ensure_csrf_cookie, 'dispatch')
@method_decorator(xframe_options_exempt, name='dispatch')
class AppEntryPoint(TemplateView):
    template_name = 'core/app_entry.html'

    def get_context_data(self, **kwargs):
        kwargs.update(assets=settings.VITE_REACT.get_assets(self.request))
        return kwargs
