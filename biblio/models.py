from django.db import models
from django.utils import timezone

class Book(models.Model):
	#author = models.ForeignKey('auth.User')
	author = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	description = models.TextField()
	borrow_date = models.DateTimeField(default=timezone.now)
	return_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.author


