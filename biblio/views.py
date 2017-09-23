from django.shortcuts import render


def books_list(request):
	return render(request, 'biblio/books_list.html', {})
