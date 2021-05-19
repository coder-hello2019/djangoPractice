from django.db import models
from django.conf import settings
# Create your models here.
# this represents each item that we have on our task list
class todoList(models.Model):
    item = models.CharField(max_length=60)
    userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 0)
