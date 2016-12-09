from django.conf.urls import url, include
from django.contrib import admin
from casas import urls as casasUrls
from main import urls as mainUrls
from django.views.static import serve
from django.conf import settings
from accounts import urls as Accounts_Urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(mainUrls, namespace="main")),
    url(r'^casas/',include(casasUrls, namespace="casas")),
    url(r'^accounts/', include(Accounts_Urls, namespace="users")),
    url(r'^api-prueba/', include('rest_framework.urls', namespace="rest_framework")),
    url(
    	regex=r'^media/(?P<path>.*)/$',
    	view=serve,
    	kwargs={"document_root":settings.MEDIA_ROOT}
    	)
]
