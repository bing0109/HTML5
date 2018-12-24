from django.db import models


# Create your models here.
class UserInfo(models.Model):
    sex = models.BooleanField(null=True, blank=True)

