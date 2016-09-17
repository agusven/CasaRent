from django.db import models
from django.contrib.auth.models import User
import secretballot

class Casa(models.Model):

	propietario = models.ForeignKey(User, blank=True,null=True)
	precio = models.IntegerField(blank=True, null=True)
	amueblada = models.BooleanField(default=True)
	servicios = models.CharField(max_length=140)
	dirección = models.CharField(max_length=140)
	cochera = models.BooleanField(max_length=140)
	recámaras = models.IntegerField(blank=True, null=True)
	plantas = models.IntegerField(blank=True, null=True)
	patio = models.BooleanField(max_length=140)
	depósito = models.IntegerField(blank=True, null=True)
	foto = models.ImageField(upload_to='fotocasa')
	teléfono = models.IntegerField(blank=True, null=True)
	fecha = models.DateField(auto_now=True)
	municipio = models.CharField(max_length=60)

	def __str__(self):
		return '{} la {} casa esta en: {}'.format(self.dirección,self.depósito,self.recámaras,self.teléfono,self.municipio)

	class Meta:
		ordering=('fecha',)


# secretballot.enable_voting_on(Casa)	