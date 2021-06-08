from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TodoItem


class TodoListView(ListView):
	model = TodoItem
	template_name = 'todo/home.html'
	context_object_name = 'todoitem'
	ordering = ['date_created']

class TodoCreateView(CreateView):
	model = TodoItem
	fields = ['author', 'item']

class TodoUpdateView(UpdateView):
	model = TodoItem
	fields = ['author', 'item']

class TodoDeleteView(DeleteView):
	model = TodoItem
	success_url = '/'

