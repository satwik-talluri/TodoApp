from django.shortcuts import render
from .models import TodoItem

def home(request):
	context = {
		'todoitem': TodoItem.objects.all(),
	}
	return render(request, 'todo/home.html', context)