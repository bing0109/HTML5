# coding=utf8
from django.db import models


# Create your models here.
class EmpInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    birth = models.DateField()
    hiredate = models.DateTimeField()
    recordtime = models.TimeField()
    hirdstatus = models.BooleanField()
    photo = models.ImageField(upload_to='media/img/')
    mail = models.EmailField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    attachments = models.FileField(upload_to='media/file/')


'''
mysql> desc testmodel_empinfo;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int(11)      | NO   | PRI | NULL    | auto_increment |
| name        | varchar(20)  | NO   |     | NULL    |                |
| age         | int(11)      | NO   |     | NULL    |                |
| birth       | date         | NO   |     | NULL    |                |
| hiredate    | datetime(6)  | NO   |     | NULL    |                |
| recordtime  | time(6)      | NO   |     | NULL    |                |
| hirdstatus  | tinyint(1)   | NO   |     | NULL    |                |
| photo       | varchar(100) | NO   |     | NULL    |                |
| mail        | varchar(254) | NO   |     | NULL    |                |
| salary      | decimal(7,2) | NO   |     | NULL    |                |
| attachments | varchar(100) | NO   |     | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
11 rows in set (0.00 sec)

'''

'''
    # 自定义表名称，默认的表名称是 项目应用名_上面的类名
    class Meta:
        db_table = 'ModelsInfo'

'''


# 出版社表
class Publisher(models.Model):
    name = models.CharField(max_length=20)
    addr = models.CharField(max_length=20)

    class Meta:
        db_table = 'publisher'


# 书表
class Book(models.Model):
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    publish_day = models.DateField()

    class Meta:
        db_tables = 'book'


# 作者
class Author(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'author'


# 作者详细信息
class AuthorDetail(models.Model):
    addr = models.CharField(max_length=20)

    class Meta:
        db_table = 'authordetail'
























