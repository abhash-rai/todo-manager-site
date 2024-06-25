from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Todo

# Create your views here.
def display_all(request):
    todo_context = {
        'todo_data': Todo.objects.all().values()
    }
    index_page = loader.get_template('index.html')
    rendered_index_page = index_page.render(todo_context, request)

    return  HttpResponse(rendered_index_page)

def view_individual(request, todo_id):
    return  HttpResponse(f'Hello {todo_id}')