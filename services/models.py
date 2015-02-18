from django.db import models

class Service(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	image = models.ImageField(upload_to='services/')

	class Meta:		
		verbose_name_plural = 'Servicios'

	def __str__(self):
		return self.title
