from django.db import models


# Create your models here.
class Translate(models.Model):
    cn = models.CharField(max_length=20)
    en = models.CharField(max_length=100)

