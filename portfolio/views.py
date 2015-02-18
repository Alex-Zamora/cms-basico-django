from django.shortcuts import render, get_object_or_404
from .models import Portfolio
from django.db.models import Count

def portfolio_detail(request, slug):
	portfolio = get_object_or_404(Portfolio, slug = slug)
	return render(request, 'portfolio_detail.html', {'portfolio': portfolio})

def portfolio_seccion(request):
	porftfolios = Portfolio.objects.all().order_by('-id')
	# popular = Portfolio.objects.annotate(Count('title'))

	return render(request, 'portfolio_seccion.html', {'portfolio': porftfolios})