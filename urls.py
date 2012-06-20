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
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
    { 'document_root': os.path.join(os.path.dirname(__file__), 'media')}),
    # Examples:
    #url(r'^$', 'condition.views.index', name='index'),
    url(r'', include('condition.catalog.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
