from django.db import models

class Technology(models.Model):
	name = models.CharField(max_length=255)

	class Meta:		
		verbose_name_plural = 'tecnologías web'

	def __str__(self):
		return self.name

class Portfolio(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	technology = models.ManyToManyField(Technology)
	imageIndex = models.ImageField(upload_to='portfolio/')
	imageProject = models.ImageField(upload_to='portfolio/')
	url = models.CharField(max_length=100, blank=True)
	slug = models.SlugField(max_length=255, blank=True)

	class Meta:		
		verbose_name_plural = 'portafolio'
	
	def get_absolute_url(self):
		return '/portafolio/%s/' % self.slug

	def __str__(self):
		return self.title

	