from rest_framework import serializers
from ..models import Casa

class CasaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Casa
		fields = ("id","propietario", "precio", "amueblada", "servicios", "direccion",
			"cochera","recamaras", "plantas","patio","deposito","foto","telefono",
			"fecha","municipio")