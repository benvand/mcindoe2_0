from django.conf.urls import url, patterns
from .views import GalleryView
urlpatterns = patterns('',
    url(r'^(?P<page_name>press|collection)/$', GalleryView.as_view(), name='gallery'),
    )