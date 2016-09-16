from django.db import models


class Casa(models.Model):

	precio = models.IntegerField(blank=True, null=True)
	amueblada = models.CharField(max_length=140)
	servicios = models.CharField(max_length=140)
	direccion = models.CharField(max_length=140)
	cochera = models.CharField(max_length=140)
	recamaras = models.CharField(max_length=140)
	plantas = models.CharField(max_length=140)
	patio = models.CharField(max_length=140)
	deposito = models.CharField(max_length=140)
	foto = models.ImageField(upload_to='fotocasa')
	telefono = models.IntegerField(blank=True, null=True)
	fecha = models.DateField(auto_now=True)
	municipio = models.CharField(max_length=60, default='Municipio')

	def __str__(self):
		return '{} la {} casa esta en: {}'.format(self.direccion,self.deposito,self.recamaras,self.telefono,self.municipio)




		


