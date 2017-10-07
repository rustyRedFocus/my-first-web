from django.contrib import admin
from .models import Book, User, Video

from django.utils import timezone
from django.shortcuts import render


def mark_available(modeladmin, request, queryset):
	queryset.update(status='a')
	queryset.update(borrow_date = timezone.now())

def mark_borrowed(modeladmin, request, queryset):
	queryset.update(status='b')
	queryset.update(borrow_date = timezone.now())

def borrow_video(modeladmin, request, queryset):
	videos = Video.objects.order_by('title')

	return render(request, 'biblio/videos_list.html', {'videos' : videos})
	




# to pozwala wyświetlić wiele pól z modelu
class BookAdmin(admin.ModelAdmin):
	list_display = ('author', 'title', 'description', 'borrow_date', 'return_date', 'status',)
	list_filter = ('borrow_date','return_date')
	ordering = ('author',)
	actions = [mark_available, mark_borrowed]
	
class UserAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name')
	actions = [borrow_video]

class VideoAdmin(admin.ModelAdmin):
	list_display = ('title', 'director', 'year',)
	

# register musi być w tej samej liście, żeby działało
admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Video, VideoAdmin)
#admin.site.register(BookAdmin)
