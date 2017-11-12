from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Book, User, Video
from .forms import VideoForm




def books_list(request):
	books = Book.objects.filter(borrow_date__lte=timezone.now()).order_by('borrow_date')
	#books = Book.objects.all()
	users = User.objects.all()


	return render(request, 'biblio/books_list.html', {'books': books, 'users' : users})

def video_detail(request, pk):
	video = get_object_or_404(Video, pk=pk)
	# pk = Primary Key, jest to alias dla atrybutu Modelu, będącego jego Primary Key
	# używa się tego zamiast "id"
	img = video.photo.url
	return render(request, 'biblio/video_detail.html', {'video' : video, 'img' : img })

def video_new(request):

	if request.method == "POST":
		form = VideoForm(request.POST, request.FILES)
		# musi byc na koncu request.FILES zeby dzialalo !!!!!!!!!!!!!!!!
		if form.is_valid():
			video = form.save(commit=False)
		#post.author = request.user
		#post.published_date = timezone.now()
			video.save()
			return redirect('video_detail', pk=video.pk)
	else:
		form = VideoForm()
	return render(request, 'biblio/video_edit.html', {'form' : form})


def video_edit(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":

        form = VideoForm(request.POST, request.FILES, instance=video)
		# musi byc na koncu request.FILES zeby dzialalo !!!!!!!!!!!!!!!!
        if form.is_valid():
            video = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            video.save()
            #return redirect('videos_detail', pk=video.pk)
            videos = Video.objects.order_by('title')
            return render(request, 'biblio/videos_list.html', {'videos' : videos})
    else:
        form = VideoForm(instance=video)
    return render(request, 'biblio/video_edit.html', {'form': form})

def borrow_video(request):
	videos = Video.objects.order_by('title')

	return render(request, 'biblio/videos_list.html', {'videos' : videos})

def video_delete(request, pk):
	v = Video.objects.get(pk=pk)
	v.delete()
	videos = Video.objects.order_by('title')
	return render(request, 'biblio/videos_list.html', {'videos' : videos})
