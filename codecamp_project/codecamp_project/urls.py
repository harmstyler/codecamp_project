from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codecamp_project.views.home', name='home'),
    # url(r'^codecamp_project/', include('codecamp_project.foo.urls')),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^speakers/', include('speakers.urls')),
    url(r'^', include('core.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
