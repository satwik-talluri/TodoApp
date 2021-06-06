from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
	auto_inc_id = models.AutoField(primary_key=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)