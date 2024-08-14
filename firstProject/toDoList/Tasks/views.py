from django.shortcuts import render,redirect
from Tasks.models import Task


# Create your views here.

def home(request):

    if request.method == 'POST':
        Task.objects.create(
            Task=request.POST['Task'],
            desc=request.POST['desc']
        )
        return redirect(home)

    data=Task.objects.all()
    context={'data':data}

    return render (request,'index.html',context)