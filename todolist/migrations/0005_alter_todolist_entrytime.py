# Generated by Django 3.2 on 2021-05-22 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_alter_todolist_entrytime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='entryTime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]