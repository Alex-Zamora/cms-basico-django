from django import template
from portfolio.models import Portfolio

register = template.Library()

# register.inclusion_tag('portafolio.html', takes_context=True)(portfolio_view)

# Registro de tags utilizando decorator
@register.inclusion_tag('portafolio.html', takes_context=True)
def portfolio_view(context):
	portfolios = Portfolio.objects.all().order_by('-id')[:3]

	return {'MEDIA_URL': context['MEDIA_URL'],'STATIC_URL': context['STATIC_URL'], 'portfolios':portfolios}