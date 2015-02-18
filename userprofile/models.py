from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name="profile")
	biography = models.TextField()
	avatar = models.ImageField(upload_to='avatar/')
	twitter = models.CharField(max_length=255, blank=True)
	facebook = models.CharField(max_length=255, blank=True)
	github = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.user.username
