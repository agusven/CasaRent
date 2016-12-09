from rest_framework import generics
from ..models import Casa
from .serializers import CasaSerializer

class Listado(generics.ListAPIView):
	queryset = Casa.objects.all()
	serializer_class = CasaSerializer