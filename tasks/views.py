from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    tasks_list = Task.objects.all()
    form = TaskForm 

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')



    context = {'tasks_list' : tasks_list , 'form': form}
    return render(request, 'tasks/index.html', context)

def update_form(request, task_id):
    task = Task.objects.get(id = task_id)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST , instance=task)
        if form.is_valid():
            form.save()

            return redirect('home')

    context = {
        'form' : form
    }
    return render(request, 'tasks/update_task.html', context)

def delete_task(request, task_id):
    task = Task.objects.get(id= task_id)
    if request.method =='POST':
        task.delete()

        return redirect('home')
    context = {
        'task': task
    }
    return render(request, 'tasks/delete.html', context)