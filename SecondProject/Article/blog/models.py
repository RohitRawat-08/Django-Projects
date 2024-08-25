from django.db import models

# Create your models here.

class DataBase(models.Model):
    Place = models.CharField(max_length=20)
    description = models.TextField()
    blog_img = models.FileField(upload_to="imgs",max_length=250,null=True,default=None)
