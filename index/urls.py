# -*- coding: utf-8 -*-
from django.urls import path
from . import views
"""
用户身份验证

Version: 0.1
Author: dsczs
"""

urlpatterns = [
    path('', views.index, name='index'),
]