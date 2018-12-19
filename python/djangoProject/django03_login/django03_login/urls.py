"""django03_login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django03_login_app import views
from django03_translate import views as views_translate


urlpatterns = [
	# url(r'^admin/', include(admin.site.urls)),
	url(r'login/', views.login),
	url(r'register/', views.register),
	url(r'register_handler/', views.register_handler),
	url(r'login_handler/', views.login_handler),
	url(r'translate/', views_translate.translateaction),
	url(r'translate_submit/', views_translate.translate_handle),
	url(r'main/', views.mainpage),
	url(r'after_register/', views.after_register)
	#后期做成，在各个应用目录下新建urls.py文件，在这里调用就行
	#url(r'',include(django03_translate.site.urls))

	]
