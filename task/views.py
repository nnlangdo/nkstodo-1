from django.shortcuts import redirect, render
from .forms import TaskForm
from .models import Task
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        'form':form,
        'tasks':tasks
    }
    return render(request, 'task/index.html', context )

def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST,instance=task)

        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        'form':form
    }
    return render(request, 'task/update_task.html',context)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect("/")
    return render(request, 'task/delete_task.html')
