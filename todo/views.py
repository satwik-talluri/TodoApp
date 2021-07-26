from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TodoItem
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


# class TodoListView(ListView):
# 	model = TodoItem
# 	template_name = 'todo/home.html'
# 	context_object_name = 'todoitem'
# 	ordering = ['auto_inc_id']

@login_required(login_url='login')
def TodoListView(request):

	items=TodoItem.objects.all().filter(author=request.user)
	context = {
		'todoitem': items
	}
	return render(request,'todo/home.html',context)

# @method_decorator(login_required, name='todo.views.TodoCreateView')
class TodoCreateView(LoginRequiredMixin, CreateView):
	login_url='login'
	model = TodoItem
	fields = ['author', 'item']

class TodoUpdateView(UpdateView):
	model = TodoItem
	fields = ['author', 'item']

class TodoDeleteView(DeleteView):
	model = TodoItem
	success_url = '/'

@login_required(login_url='login')
def TodoGetView(request):
	a = request.GET.get('ID')
	a=int(a)
	items=TodoItem.objects.all().filter(auto_inc_id=a).first()
	context = {
		'todoitems': items
	}
	return render(request,'todo/todo_get.html',context)

@login_required(login_url='login')
def TodoGetAll(request):
	if request.user.is_superuser:
		items=TodoItem.objects.all()
	else:
		items=TodoItem.objects.all().filter(author=request.user)
	context = {
		'todoitems': items
	}

	return render(request,'todo/todo_getall.html',context)
