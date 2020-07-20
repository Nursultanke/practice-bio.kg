from django.urls import path, include

from pages.views import IndexView, NewsView, AboutView, GalleryView, ProjectsView, \
    FeedBackView, ContactView, VideoView, BlogView, VideoInnerView, BlogInnerView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('news/', NewsView.as_view(), name='news'),
    path('about/', AboutView.as_view(), name='about'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('feedback/', FeedBackView.as_view(), name='feedback'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('video/', VideoView.as_view(), name='video'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('video_inner/', VideoInnerView.as_view(), name='video_inner'),
    path('blog_inner/', BlogInnerView.as_view(), name='blog_inner'),
]
