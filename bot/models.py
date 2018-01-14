from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	session = models.CharField(max_length=15)
	message = models.CharField(max_length=200)
	isUserCreated=models.BooleanField()
	def __unicode__(self):
		return self.message
