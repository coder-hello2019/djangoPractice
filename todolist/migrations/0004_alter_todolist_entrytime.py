# Generated by Django 3.2 on 2021-05-22 16:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_todolist_entrytime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='entryTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 22, 16, 51, 40, 267747, tzinfo=utc)),
        ),
    ]
