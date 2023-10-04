from re import T
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404
from .models import Todo
from .forms import TodoForm

# Create your views here.
@csrf_protect
def register_todos(request):
  form = TodoForm(request.POST)
  if form.is_valid():
      todo = Todo()
      todo.description = form.cleaned_data['description']
      todo.status = "pendente"
      todo.save()
      return render(request, 'register_todos.html', {'form': form})
  
  return render(request, 'register_todos.html', {'form': form})

def list_todos(request):
    todos = Todo.objects.all()
    return render(request, 'list_todos.html', {'todos': todos})


def atualizar_status_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    
    # Atualize o status do todo para "Concluído"
    todo.status = "Concluído"
    todo.save()
    
    # Redirecione de volta para a página de detalhes do cliente
    # return redirect('detalhes_cliente', cliente_id=pedido.cliente.id)
    return redirect('list_todos')


def excluir_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    
    # Atualize o status do todo para "Concluído"
    todo.delete()
    
    # Redirecione de volta para a página de detalhes do cliente
    # return redirect('detalhes_cliente', cliente_id=pedido.cliente.id)
    return redirect('list_todos')