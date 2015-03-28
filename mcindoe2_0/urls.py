from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mcindoe2_0.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('apps.staticpage.urls')),
    url(r'', include('apps.gallery.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/collection/')),
)
