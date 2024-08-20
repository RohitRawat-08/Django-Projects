from django.db import models

# Create your models here.

class DataBase(models.Model):
    Place = models.CharField(max_length=20)
    description = models.TextField()
