# Generated by Django 2.1.4 on 2018-12-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodel', '0003_book_hot_pric'),
    ]

    operations = [
        migrations.AddField(
            model_name='authordetail',
            name='isdelete',
            field=models.BooleanField(default=False),
        ),
    ]