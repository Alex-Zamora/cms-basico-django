from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Post

def post_detail(request, slug):
	post = get_object_or_404(Post, slug = slug)

	return render(request, 'post_detail.html', {'post_detail':post})

def post_seccion(request):
	post_list = Post.objects.all().order_by('-id')

	paginator = Paginator(post_list,9)

	try: 
		pagina = int(request.GET.get('page','1')) #liena importante
	except ValueError: pagina = 1

	try: 
		post_list = paginator.page(pagina) #liena importante
	except (InvalidPage, EmptyPage):
		post_list = paginator.page(paginator.num_pages)

	return render(request, 'post_seccion.html', {'post_list':post_list})

