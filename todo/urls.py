from django.urls import path
from .views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoGetView, TodoGetAll

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-home'),
    path('new/', TodoCreateView.as_view(), name='todo-create'),
    path('todo_get/<int:pk>/update', TodoUpdateView.as_view(), name='todo-update'),
    path('todo_get/<int:pk>/delete', TodoDeleteView.as_view(), name='todo-delete'),
    path('todo_get/', TodoGetView, name='todo-get'),
    path('todo_getall/', TodoGetAll, name='todo-getall')
]