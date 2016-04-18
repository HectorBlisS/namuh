from django.conf.urls import url,include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from shop import urls as shopUrls
from cart import urls as cartUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shop/',
    	include(shopUrls,namespace='shop')),
    url(r'^cart/',
    	include(cartUrls,namespace='cart')),

]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)