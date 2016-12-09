from django.conf.urls import url, include
from . import views
from .api import urls as urlsAPI

urlpatterns = [
	url(r'^$', views.Home.as_view(), name="list"),
	url(r'^(?P<pk>\d+)/$', views.CasaDetail.as_view(),name="detail"),
	url(r'^nuevo/$', views.CasaCreation.as_view(), name="new"),
	url(r'^editar/(?P<pk>\d+)/$', views.CasaUpdate.as_view(), name="update"),
	url(r'^borrar/(?P<pk>\d+)/$', views.CasaDelete.as_view(), name="delete"),
	url(r'^api/', include(urlsAPI, namespace="api")),
]
