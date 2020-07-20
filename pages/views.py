from django.shortcuts import render
from django.views.generic import TemplateView

from health_principle.models import HealthPrinciple


class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get(self, request, *args, **kwargs):
        principles = HealthPrinciple.objects.all()
        return render(request, self.template_name, context={
            'principles': principles
        })


class NewsView(TemplateView):
    template_name = 'pages/news.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})
