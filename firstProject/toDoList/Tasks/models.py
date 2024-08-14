from django.db import models

# Create your models here.


class Task(models.Model):
    Task = models.CharField(max_length=30)
    desc = models.CharField(max_length=70)
