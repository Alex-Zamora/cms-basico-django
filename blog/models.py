from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=255)

	class Meta:		
		verbose_name_plural = 'categorías'

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	imageIndex = models.ImageField(upload_to='blog/')
	imagePost = models.ImageField(blank=True, upload_to='blog/')
	slug = models.SlugField(max_length=255, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User)
	category = models.ManyToManyField(Category)

	class Meta:		
		verbose_name_plural = 'Entradas del blog'

	def get_absolute_url(self):
		return '/blog/%s/' % self.slug

	# def save(self, *args, **kwargs):
	# 	self.slug = self.slug.lower().replace(' ','-')
	# 	super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title


