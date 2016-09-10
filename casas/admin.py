from django.contrib import admin
from .models import Casa

# Register your models here.
class CasaAdmin(admin.ModelAdmin):
	list_display = ['id','precio','direccion','amueblada','servicios','cochera','recamara','plantas','patio','depocito']

admin.site.register(Casa, CasaAdmin)