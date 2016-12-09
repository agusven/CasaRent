from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User

class Profile(models.Model):
		user = models.OneToOneField(User)
		municipio = models.CharField(max_length=140,blank=True,null=True)
		cellphone = models.IntegerField(blank=True, null=True)
		image_back = models.ImageField(upload_to="user/back", blank=True, null=True)
		image_profile = models.ImageField(upload_to="user/profile", blank=True, null=True)

		def __str__(self):
			return 'Perfil del usuario {}'.format(self.user.username)

# Create your models here.p