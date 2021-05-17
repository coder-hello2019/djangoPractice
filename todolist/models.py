from django.db import models

# Create your models here.
# this represents each item that we have on our task list
class todoList(models.Model):
    item = models.CharField(max_length=60)
