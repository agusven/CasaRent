from django import template
from ..models import Casa

register = template.Library()

@register.simple_tag
def colonia():
	return Casa.objects.get(id=1).municipio

#@register.inclusion_tag('casa/tag.html')
#def ultimo(count=2):
	#ultimos_municipios = Casa.objects.all().order_by('fecha')[:count]
	#return {'ultimos_municipios':ultimos_municipios}


@register.assignment_tag
def ultimos(count=3):
	return Casa.objects.all().order_by('-fecha')[:count]