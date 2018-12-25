# coding=utf8

"""django06_1224_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from testviews import views
from boke1225 import views as bkviews


urlpatterns = [
    path('admin/', admin.site.urls),
    url('form1/', views.form1),
    url('form1_handle/', views.form1_handle),
    url('verfypic/', views.verifycode),
    url('index/(\d*)', bkviews.bk_index),
    url('new_boke/', bkviews.new_boke),
    url('new_bk_submit/', bkviews.new_bk_submit),
    url('ar_delete/(\d*)', bkviews.ar_delete),
    url('ar_modify/(\d*)', bkviews.ar_modify)
]
