from portfolio.models import Portfolio
from blog.models import Post

def basico(request):
	projects = Portfolio.objects.all()
	# Se inicializa la variable
	project = None
	# request.path mestra la url en que se esta ubicado
	path = request.path
	for p in projects:
		if path == p.get_absolute_url():
			project = p
			# break para finalizar el if
			break
	return {'titulo':'Mi Página web', 'path':path, 'project_url': project}

#post_url obtiene la url del post
def basico2(request):
	entradas = Post.objects.all()
	entrada = None
	path = request.path
	for e in entradas:
		if path == e.get_absolute_url():
			entrada = e
			break
	return {'post_url': entrada}