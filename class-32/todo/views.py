from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    db_todos = Todo.objects.all()

    return render(
        request=request,
        template_name='todo/todo_list.html', 
        context={'todos' : db_todos}
    )


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
       form = TodoForm()

    return render(
        request=request,
        template_name='todo/todo_create.html',
        context={'form' : form}
    ) 


def update_todo(request, pk):
    todo =get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
       form = TodoForm(instance=todo)

    return render(
        request=request,
        template_name='todo/todo_create.html',
        context={'form' : form}
    )

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    todo.delete()
    return redirect('todo_list')