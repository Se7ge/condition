import os.path
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #('^$', search),
    (r'^ckeditor/', include('ckeditor.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    { 'document_root': os.path.join(os.path.dirname(__file__), 'static')}),
    # Examples:
    # url(r'^$', 'condition.views.home', name='home'),
    # url(r'^condition/', include('condition.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)