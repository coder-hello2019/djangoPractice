# Generated by Django 3.2 on 2021-05-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_alter_todolist_entrytime'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='associatedProject',
            field=models.CharField(default='No Project', max_length=60),
        ),
    ]
