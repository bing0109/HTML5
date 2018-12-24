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
    publish = models.ForeignKey(to='Publisher', on_delete=models.CASCADE)
    hot_price = models.DecimalField(max_digits=7, decimal_places=2, default=99.99)
    isdelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'book'


# 作者
class Author(models.Model):
    name = models.CharField(max_length=20)
    book = models.ManyToManyField(to='Book')
    author_detail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)

    class Meta:
        db_table = 'author'


# 作者详细信息
class AuthorDetail(models.Model):
    addr = models.CharField(max_length=20)
    isdelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'authordetail'


# 1220作业的表格
class Student(models.Model):
    """学生表"""
    name = models.CharField(max_length=100)
    gender = models.SmallIntegerField()

    class Meta:
        db_table = 'student'


class Course(models.Model):
    """课程表"""
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'course'


class Score(models.Model):
    """分数表"""
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    number = models.FloatField()

    class Meta:
        db_table = 'score'


class Teacher(models.Model):
    """老师表"""
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'teacher'


# 设置字段可为空，null=True
# 设置admin后台管理添加字段可为空 blank=True
class Nulltest(models.Model):
    attr1 = models.CharField('字段1', max_length=20)
    attr2 = models.CharField('字段2', max_length=20, null=True)
    attr3 = models.CharField('字段3', max_length=20, null=True, blank=True)













