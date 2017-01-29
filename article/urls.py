# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from article.views import *


urlpatterns = [
    url(r'get/(?P<pk>\d+)/$', article),
    url(r'^article/addcomment/(?P<pk>\d+)/$', addcomment),
    url(r'', ArticlesList.as_view()),
]