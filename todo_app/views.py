from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo
from django.urls import reverse

# Create your views here.

def index(request):
    all_todo = Todo.objects.all()
    return render(request,'todo_app/index.html', {"Todo" : all_todo})


def addtodo(request):
    if request.method == 'POST':
        todo_title = request.POST['todo_title']
        todo_description = request.POST['todo_description']
        Todo.objects.create(title=todo_title, description=todo_description)
        return HttpResponseRedirect(reverse('todo_app:index'))
    else:
        return HttpResponseRedirect(reverse('todo_app:index'))


def deletetodo(request, id):
    Todo.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('todo_app:index'))


def marktodo(request, id):
    todo_item = Todo.objects.get(id=id)
    todo_item.completed = True
    todo_item.save()
    return HttpResponseRedirect(reverse('todo_app:index'))


def unmarkedtodo(request, id):
    todo_item = Todo.objects.get(id=id)
    todo_item.completed = False
    todo_item.save()
    return HttpResponseRedirect(reverse('todo_app:index'))