from django.db import models

class Casa(models.Model):

	precio = models.CharField(max_length=140)
	amueblada = models.BooleanField(default=True)
	servicios = models.BooleanField(default=True)
	direccion = models.CharField(max_length=140)
	cochera = models.BooleanField(default=True)
	recamara = models.CharField(max_length=140)
	plantas = models.CharField(max_length=140)
	patio = models.BooleanField(default=True)
	depocito = models.CharField(max_length=140)
	foto = models.ImageField(upload_to='fotocasa')


	def __str__(self):
		return '{} la {} casa esta en: {}'.format(self.direccion,self.depocito,self.recamara)




		


