from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category

class PostAdmin(SummernoteModelAdmin):
	pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category)