from django.db import models

# Create your models here.
class todoList(models.Model):
    item = models.CharField(max_length=60)
    PRIORITIES = (('L', 'Low'), ('M', 'Medium'), ('H', 'High'))
