from django.shortcuts import render
from contacto.forms import ContactForm
from django.template import RequestContext

def contacto_seccion(request):
	form = ContactForm()
	return render(request, 'contacto.html', {'form': form})