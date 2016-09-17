from django.db import models


class Casa(models.Model):

	SERVICIOS_CHOISES = (('Luz','Luz'),('Gas','Gas'),('Teléfono','Teléfono'),('Agua','Agua'))
	precio = models.IntegerField(blank=True, null=True)
	amueblada = models.BooleanField(default=True)
	servicios = models.CharField(max_length=140)
	direccion = models.CharField(max_length=140)
	cochera = models.BooleanField(max_length=140)
	recamaras = models.IntegerField(blank=True, null=True)
	plantas = models.IntegerField(blank=True, null=True)
	patio = models.BooleanField(max_length=140)
	deposito = models.IntegerField(blank=True, null=True)
	foto = models.ImageField(upload_to='fotocasa')
	telefono = models.IntegerField(blank=True, null=True)
	fecha = models.DateField(auto_now=True)
	municipio = models.CharField(max_length=60)

	def __str__(self):
		return '{} la {} casa esta en: {}'.format(self.direccion,self.deposito,self.recamaras,self.telefono,self.municipio)




		


