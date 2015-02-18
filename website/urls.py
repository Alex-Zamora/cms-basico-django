from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   

    url(r'^admin/', include(admin.site.urls)),
    #Summernote editor WYSIWYG 
    (r'^summernote/', include('django_summernote.urls')),
    url(r'^$', 'services.views.service_view', name='home'),
    url(r'^portafolio/(?P<slug>[\w\-]+)/', 'portfolio.views.portfolio_detail', name='portfolio_detail'),
    url(r'^portafolio/', 'portfolio.views.portfolio_seccion', name='portfolio_seccion'),
    url(r'^blog/(?P<slug>[\w\-]+)/', 'blog.views.post_detail', name='post_detail'),
    url(r'^blog/', 'blog.views.post_seccion', name='post_seccion'),
    url(r'^contacto/', 'contacto.views.contacto_seccion', name='contacto_seccion'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
)
