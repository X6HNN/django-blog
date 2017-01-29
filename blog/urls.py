from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'auth/', include('login.urls')),
    url(r'articles/', include('article.urls')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^works/$', TemplateView.as_view(template_name='works.html')),
    url(r'', include('article.urls')),
]