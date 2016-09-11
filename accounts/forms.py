from django import forms
from django.contrib.auth.models import User 
from .models import Profile

class SignInForm(forms.ModelForm):
	password = forms.CharField(label="Password", widget=forms.PasswordInput)
	password_again = forms.CharField(label="Ingresa nuevamente tu constraseña", widget=forms.PasswordInput)

	class Meta:
		model = User 
		fields = ('username','first_name', 'email',)

	def clean_password_again(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password_again']:
			raise forms.ValidationError('Las contraseñas no coinciden')
		return cd['password_again']

class EditUserForm(forms.ModelForm):
	first_name = forms.CharField(label = "Nombre")
	last_name = forms.CharField(label = "Apellidos")
	email = forms.CharField(label="Correo Electrónico")
	class Meta:	
		model = User 
		fields = ['first_name','last_name','email']

class EditProfileForm(forms.ModelForm):
	cellphone_number = forms.CharField(label="Teléfono")
	date_birth = forms.CharField(label='Fecha de Nacimiento')
	image_back = forms.ImageField(label = 'Foto de portada', widget=forms.FileInput(attrs={'class': 'imageprofile'}))
	image_profile = forms.ImageField(label = 'Foto de perfil', widget=forms.FileInput(attrs={'class': 'imageprofile'}))
	class Meta:
		model = Profile
		fields = ['cellphone_number','date_birth', 'image_back', 'image_profile']