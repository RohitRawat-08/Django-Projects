from django.shortcuts import render
from blog.models import DataBase

# Create your views here.

def home(request):
    blog = DataBase.objects.all()
    context = {'data': blog}
    return render(request, "home.html",context)


def display(request,id):
    blog = DataBase.objects.get(id = id)
    context = {'value': blog}
    return render(request,"display.html",context)




