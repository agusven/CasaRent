from django.conf.urls import url
from django.contrib.auth.views import login, logout, logout_then_login 
from . import views

urlpatterns = [
	
		url(r'^profile/$', views.Profile2.as_view(), name="profile"),
	 	url(r'^sign-in/$', views.Sign_In.as_view(), name="signin"),
	 	url(r'^login/$', login, name="login"),
	 	url(r'^logout/$', logout, name="logout"),
	 	url(r'^logout-then-login/$', logout_then_login, name="logout-then-login"),
	 	url(r'^(?P<user>.*)$', views.UserProfile.as_view(), name="user-profile"),

]