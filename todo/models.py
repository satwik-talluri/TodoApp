from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class TodoItem(models.Model):
	auto_inc_id = models.AutoField(primary_key=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.auto_inc_id

	def get_absolute_url(self):
		return ('/')