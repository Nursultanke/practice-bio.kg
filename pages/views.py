from django.shortcuts import render
from django.views.generic import TemplateView

from health_principle.models import HealthPrinciple, Statistic


class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get(self, request, *args, **kwargs):
        principles = HealthPrinciple.objects.all()
        statistics = Statistic.objects.all()
        return render(request, self.template_name, context={
            'principles': principles,
            'statistics': statistics

        })


# class StatisticView(TemplateView):
#     template_name = 'pages/index.html'
#
#     def get(self, request, *args, **kwargs):
#         statistics = Statistic.objects.all()
#         return render(request, self.template_name, context={
#             'statistics': statistics
#         })


class NewsView(TemplateView):
    template_name = 'pages/news.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class GalleryView(TemplateView):
    template_name = 'pages/gallery.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class ProjectsView(TemplateView):
    template_name = 'pages/projects.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class FeedBackView(TemplateView):
    template_name = 'pages/feedback.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class ContactView(TemplateView):
    template_name = 'pages/contacts.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class VideoView(TemplateView):
    template_name = 'pages/video.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class BlogView(TemplateView):
    template_name = 'pages/blog.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class VideoInnerView(TemplateView):
    template_name = 'pages/video_inner.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class BlogInnerView(TemplateView):
    template_name = 'pages/blog_inner.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})