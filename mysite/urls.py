from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from .settings import MEDIA_ROOT
from blog import views



urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
    	{'document_root': MEDIA_ROOT}),
    url(r'^about/$', views.flatpage,  name='about'),
    
    
    #url(r'^pages/', include('django.contrib.flatpages.urls')),
    
    
    

]


