from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Todo
from .forms import TodoForm

# Create your views here.
def display_all(request):
    todo_context = {
        'todo_data': Todo.objects.all().values()
    }
    index_page = loader.get_template('index.html')
    rendered_index_page = index_page.render(todo_context, request)

    return  HttpResponse(rendered_index_page)

def view_individual(request, todo_id):
    
    if (request.method == 'GET'):
        try:
            to_update_todo_item = Todo.objects.get(id=todo_id)
        except:
            return HttpResponse(f'No such item found with id {todo_id}')
        else:
            to_update_form = TodoForm(instance=to_update_todo_item)

            context ={
                'form': to_update_form
            }

            update_page = loader.get_template('view_individual.html')
            return HttpResponse(update_page.render(context, request))
        
    elif (request.method == 'POST'):
        try:
            to_update_todo_item = Todo.objects.get(id=todo_id)
        except:
            return HttpResponse(f'No such item found with id {todo_id}')
        else:
            to_update_form = TodoForm(request.POST, instance=to_update_todo_item)
            if to_update_form.is_valid():
                to_update_form.save()
                return HttpResponseRedirect('/')  # You can also Redirect here


def create(request):
    
    if (request.method == 'GET'):
        context ={
            'form': TodoForm()
        }

        create_page = loader.get_template('create_todo.html')
        rendered_create_page = create_page.render(context, request)
        return HttpResponse(rendered_create_page)

    # Create
    elif (request.method == 'POST'):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/") # redirect example



def delete_individual(request, todo_id):

    if (request.method == 'GET'):
        update_page = loader.get_template('delete_individual.html')
        context = {}
        return HttpResponse(update_page.render(context, request))
        
    elif (request.method == 'POST'):
        try:
            to_update_todo_item = Todo.objects.get(id=todo_id)
        except:
            return HttpResponse(f'No such item found with id {todo_id}')
        else:
            to_update_todo_item.delete()
            return HttpResponseRedirect('/')  # You can also Redirect here