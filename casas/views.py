from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Casa
from django.core.urlresolvers import reverse_lazy

class Home(ListView):
	model = Casa
	template_name = 'casa/casa_list.html'

class CasaDetail(DetailView):
	model = Casa
	template_name = 'casa/casa_detail.html'

class CasaCreation(CreateView):
	model = Casa
	success_url = reverse_lazy('casas:list')
	fields = ['direccion','municipio','telefono','precio','servicios','recamaras','plantas','amueblada','cochera','patio','deposito','foto']
	template_name = 'casa/casa_form.html'

class CasaUpdate(UpdateView):
	model = Casa
	success_url = reverse_lazy('casas:list')
	fields = ['municipio','precio','direccion','amueblada','servicios','cochera','recamaras','plantas','patio','deposito','foto','telefono']
	template_name = 'casa/casa_form.html'


class CasaDelete(DeleteView):
	model =Casa
	success_url = reverse_lazy('casas:list')
	template_name = 'casa/casa_confirm_delete.html'
	