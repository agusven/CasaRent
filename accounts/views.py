from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import SignInForm, EditProfileForm, EditUserForm
from django.contrib.auth.models import User

class Sign_In(View):
	def get(self, request):
		template_name = "accounts/sign_in.html"
		form = SignInForm()
		context = {'form':form,}
		return render(request, template_name, context)
	def post(self,request):
		template_name="accounts/sign_in.html"
		signin_form = SignInForm(request.POST)
		if signin_form.is_valid():
			signin = signin_form.save(commit=False)
			signin.set_password(signin_form.cleaned_data['password'])
			signin.save()
			profil = Profile()
			print(signin)	
			profil.user = signin
			print(profil.user)
			profil.save()

			return redirect('users:login')
		else:
			context = {'form':signin_form,}
			return render(request, template_name, context)


class Profile2(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = "accounts/profile.html"
		userform = EditUserForm(instance=request.user)
		profileform = EditProfileForm(instance=request.user.profile)
		context = {'userform':userform, 'profileform':profileform,}
		return render(request, template_name, context)
	def post(self, request):
		template_name = "accounts/profile.html"
		updateUser_form = EditUserForm(data=request.POST, instance=request.user)
		updateProfile_form = EditProfileForm(data=request.POST, instance=request.user.profile, files=request.FILES)
		if updateUser_form.is_valid():
			updateUser = updateUser_form.save(commit=False)
			updateUser.save()
		if updateProfile_form.is_valid():
			updateProfile = updateProfile_form.save(commit=False)
			updateProfile.save()
		return redirect('users:profile')

class UserProfile(View):
	@method_decorator(login_required)
	def get(self,request,user):
		template_name = "accounts/userprofile.html"
		user_data = User.objects.get(username=user)
		context = {'user_data':user_data}
		return render(request, template_name, context)






# Create your views here.
