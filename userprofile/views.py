from django.shortcuts import render

def profile_view(request):
	profile = UserProfile.objects.all()

	return render(request, 'profile.html', {'profile':profile})
