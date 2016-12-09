from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Casa
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class Home(ListView):
	model = Casa
	template_name = 'casa/casa_list.html'

class CasaDetail(DetailView):
	model = Casa
	template_name = 'casa/casa_detail.html'

@method_decorator(login_required, name='dispatch')
class CasaCreation(CreateView):
	model = Casa
	success_url = reverse_lazy('casas:list')
	fields = ['direccion','municipio','telefono','precio','servicios','recamaras','plantas','amueblada','cochera','patio','deposito','foto']
	template_name = 'casa/casa_form.html'

	def form_valid(self, form):
		form.instance.propietario = self.request.user
		return super(CasaCreation, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class CasaUpdate(UpdateView):
	model = Casa
	success_url = reverse_lazy('casas:list')
	fields = ['direccion','municipio','telefono','precio','servicios','recamaras','plantas','amueblada','cochera','patio','deposito','foto']
	template_name = 'casa/casa_form.html'

@method_decorator(login_required, name='dispatch')
class CasaDelete(DeleteView):
	model = Casa
	success_url = reverse_lazy('casas:list')
	template_name = 'casa/casa_confirm_delete.html'
	