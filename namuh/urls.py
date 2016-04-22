from django.conf.urls import url,include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from shop import urls as shopUrls
from cart import urls as cartUrls
from orders import urls as ordersUrls
from main import urls as mainUrls
from paypal.standard.ipn import urls as paypalUrls
from payment import urls as paymentUrls



urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^paypal/',
        include(paypalUrls)),
    url(r'^payment/',
        include(paymentUrls,namespace='payment')),

    url(r'^shop/',
    	include(shopUrls,namespace='shop')),
    url(r'^cart/',
    	include(cartUrls,namespace='cart')),
    url(r'^orders/',
    	include(ordersUrls,namespace='orders')),
    url(r'^',
    	include(mainUrls,namespace='main')),

    url(
        regex=r'^media/(?P<path>.*)$',
        view='django.views.static.serve',
        kwargs={'document_root':settings.MEDIA_ROOT}),

]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)