from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('post.html', takes_context=True)
def post_view(context):
	post = Post.objects.all().order_by('-id')[:3]
	return{'MEDIA_URL': context['MEDIA_URL'], 'STATIC_URL': context['STATIC_URL'], 'posts':post}
	
# register.inclusion_tag('post.html')(post_view)