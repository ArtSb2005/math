from django.views.generic import ListView

from ege.models import variant_ege


class EgePageView(ListView):
    model = variant_ege
    template_name = 'ege.html'
