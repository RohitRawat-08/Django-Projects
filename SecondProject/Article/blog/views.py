from django.shortcuts import render
from blog.models import DataBase

# Create your views here.

def home(request):
    blog = DataBase.objects.all()
    context = {'data': blog}
    return render(request, "home.html",context)


def display(request):
    return render(request,"display.html")




# def index(request):
#     blog=Article.objects.all()
#     context={'data':blog}
#     return render(request,'index.html',context)