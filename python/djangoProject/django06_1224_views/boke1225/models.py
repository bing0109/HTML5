# coding=utf8

from django.db import models


# Create your models here.
class Article(models.Model):
    ar_title = models.CharField(max_length=30)
    ar_brief = models.CharField(max_length=150, null=True, blank=True)
    ar_content = models.CharField(max_length=10240)
    ar_create_time = models.DateTimeField(auto_now=True)
    ar_update_time = models.DateTimeField(null=True, blank=True)
    author_id = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE)


class Comment(models.Model):
    comm_text = models.CharField(max_length=300)
    comm_time = models.DateTimeField(auto_now=True)
    article_id = models.ForeignKey(to='Article', on_delete=models.CASCADE)
    author_id = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE)


class UserInfo(models.Model):
    us_name = models.CharField(max_length=20)
    us_pswd = models.CharField(max_length=128)
    us_register_time = models.DateTimeField(auto_now=True)
    us_nickname = models.CharField(max_length=20)
    us_photo = models.ImageField(null=True, blank=True)
