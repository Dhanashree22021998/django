from django.shortcuts import render,redirect
from . models import Task
from .forms import TaskForm,TaskCompleteForm

def addview(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/v1/s1/')
    return render(request,'app1/add.html',{'form':form})        

def showview(request):
    obj = Task.objects.all()
    return render(request,'app1/show.html',{'obj':obj})

def updateview(request,pk):
    obj=Task.objects.get(pk=pk)
    form = TaskCompleteForm(instance=obj)
    if request.method == 'POST':
        form = TaskCompleteForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/v1/s1/')
    return render(request,'app1/add.html',{'obj' : obj,"form":form})


def deleteview(request,pk):
    obj = Task.objects.get(pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/v1/s1/')
    return render(request,"app1/confirm.html",{"obj":obj})    
