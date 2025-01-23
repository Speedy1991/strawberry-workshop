from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView

from core.load_vite_app import AppLoader


@method_decorator(ensure_csrf_cookie, 'dispatch')
class AppEntryPoint(TemplateView):
    template_name = 'core/app_entry.html'

    def get_context_data(self, **kwargs):
        kwargs['assets'] = AppLoader('js-bundles/react/index.html', port=4201, bundle='REACT').assets(self.request)
        return kwargs
