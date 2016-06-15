from django import template
from ..models import Post

register = template.Library()


@register.inclusion_tag('starter_app/navigation.html')
def menubar(active=None):
	return { 
		'posts': Post.objects.all(),
		'active': active
		}
