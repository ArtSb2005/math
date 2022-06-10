from django.views.generic import TemplateView, ListView

from oge.models import variant_oge


class OgePageView(ListView):
    model = variant_oge
    template_name = 'oge.html'
