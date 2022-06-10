from django.views.generic import TemplateView, ListView

from main.models import cert_main


class HomePageView(ListView):
    model = cert_main
    template_name = 'index.html'
