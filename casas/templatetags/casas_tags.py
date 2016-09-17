from django import template
from ..models import Casa

register = template.Library()

@register.simple_tag
def numCasas():
	return Casa.objects.all().count()

@register.assignment_tag
def ultimos(count=3):
	return Casa.objects.all().order_by('-fecha')[:count]


@register.assignment_tag(takes_context=True)
def cerca_de_ti(context, count=3):
	request = context['request']
	municipio = request.user.profile.municipio
	var = Casa.objects.filter(municipio=municipio).order_by('-fecha')[:count]
	return var 

