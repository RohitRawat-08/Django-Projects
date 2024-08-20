from django.contrib import admin
from blog.models import DataBase


# Register your models here.

class DataBaseAdmin(admin.ModelAdmin):
    list_display=['id','Place','description']


admin.site.register(DataBase,DataBaseAdmin)