from django.conf.urls import url
from . import views



urlpatterns=[
	url(r'^create/$',
		views.OrderCreate.as_view(),
		name="order_create"),
	
]