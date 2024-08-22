from django.shortcuts import render, redirect, get_object_or_404
from App.models import Task
from django.views.generic import UpdateView

# Create your views here.

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    
    context = {
        'tasks': tasks,
        'completed_tasks' : completed_tasks
    }
    return render(request, 'home.html', context)



def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')



def done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def back(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        return render(request, 'edit.html', {'get_task': get_task})


def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')