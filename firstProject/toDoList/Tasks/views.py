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



def edit(request ,id):
    data=Task.objects.get(id=id)

    if request.method == 'POST':
        data.Task=request.POST['Task']
        data.desc=request.POST['desc']
        data.save()
        return redirect(home)

    context ={'data':data}
    return render (request, 'form.html',context)


def delete(request ,id):
    data=Task.objects.get(id=id)
    
    if request.method == 'POST':
        data.delete()
        return redirect(home)

    return render(request,'delete.html')



