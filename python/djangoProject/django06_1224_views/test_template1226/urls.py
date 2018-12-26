# coding:utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url('login/', views.login),
    url('register/', views.register),
    url('userinfo/', views.user_center_info),
    url('userorder/', views.user_center_order),
    url('usersite/', views.user_center_site)
]
