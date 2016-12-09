from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^listado/$', views.Listado.as_view(), name="listado_api")
]