from django.conf.urls import url, patterns
from .views import StaticPageView
urlpatterns = patterns('',
    url(r'^(?P<page_name>about|contact)/$', StaticPageView.as_view(), name='static_page'),
    )