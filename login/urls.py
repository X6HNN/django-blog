# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from login.views import *


urlpatterns = [
    url(r'login/$', login),
    url(r'logout/$', logout),
]