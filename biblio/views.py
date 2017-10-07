from django.shortcuts import render
from django.utils import timezone
from .models import Book, User


def books_list(request):
	books = Book.objects.filter(borrow_date__lte=timezone.now()).order_by('borrow_date')
	#books = Book.objects.all()
	users = User.objects.all()


	return render(request, 'biblio/books_list.html', {'books': books, 'users' : users})
