from django.shortcuts import render
from .models import Service


def service_view(request):
	service = Service.objects.all()

	return render(request, 'servicios.html', {'service':service})


