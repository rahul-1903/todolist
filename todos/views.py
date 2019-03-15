from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

from datetime import date
# Create your views here.

def index(request):
    todos = Todo.objects.all()[:10]

    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }

    return render(request, 'details.html', context)

def add(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        due_date = request.POST['due_date']
        todo = Todo(title=title,text=text, due_date=due_date)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html', {})    

def delete(request, id):
    Todo.objects.filter(id=id).delete()
    
    
    return redirect('/todos')

def complete(request, id):
    todo = Todo.objects.get(id=id)
    if todo.complete:
        todo.complete = False
    else:
        todo.complete = True
    todo.save()

    return redirect('/todos')
