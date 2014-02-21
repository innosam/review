from django.conf.urls import patterns, include, url
from django.contrib import admin
import allauth

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cisco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^review/', include('review.urls')),
    url(r'^accounts/', include('allauth.urls')),
)
