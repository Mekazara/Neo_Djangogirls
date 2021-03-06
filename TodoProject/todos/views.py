import imp
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .models import ToDo



# Create your views here.

def list_todo_items(request):
    context = { 'todo_list':ToDo.objects.all() }
    return render(request, 'todos/todo_list.html', context)

def insert_todo_item(request:HttpRequest):
    todo = ToDo(content = request.POST['content'])
    todo.save()
    return redirect('/todos/list/')

def delete_todo_item(request, todo_id):
    todo_to_delete = ToDo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')