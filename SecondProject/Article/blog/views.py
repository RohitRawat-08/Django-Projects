from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")


def display(request):
    return render(request,"display.html")