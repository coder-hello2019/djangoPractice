from django.db import models
from django.conf import settings
from datetime import timedelta, datetime
# to make timezones django-compliant
from django.utils.timezone import make_aware, now

# Create your models here.
# this represents each item that we have on our task list
class todoList(models.Model):
    item = models.CharField(max_length=60)
    userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 0)
    duration = models.DurationField(default=timedelta(hours=0, minutes=0, seconds=0))
    entryTime = models.DateTimeField(default=datetime.now)
    associatedProject = models.CharField(max_length=60, default="No Project") 
