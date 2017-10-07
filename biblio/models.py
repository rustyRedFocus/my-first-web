from django.db import models
from django.utils import timezone
import datetime

borrow_lenght = timezone.now() + datetime.timedelta(days=30)


class Book(models.Model):
	#author = models.ForeignKey('auth.User')
	author = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	description = models.TextField()
	borrow_date = models.DateTimeField(default=timezone.now)
	return_date = models.DateTimeField(default=borrow_lenght)
	#return_date = models.DateTimeField(blank=True, null=True)

	STATUS_CHOICES = (
		('b', 'Borrowed'),
		('a', 'Available')
	)
	status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='a')



	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	def __str__(self):
		return self.last_name


class Video(models.Model):
	title = models.CharField(max_length=200)
	director = models.CharField(max_length=200)
	year = models.CharField(max_length=4)

	STATUS_CHOICES = (
		('b', 'Borrowed'),
		('a', 'Available')
	)
	status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='a')


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title