from django.conf.urls import url
from . import views


urlpatterns=[
	url(r'^$',
		views.Home.as_view(),
		name="home"),
	url(r'^nosotros/$',
		views.Nosotros.as_view(),
		name="nosotros"),
	url(r'^puntos/$',
		views.Selling.as_view(),
		name="selling"),
	url(r'^politicas/$',
		views.Policies.as_view(),
		name="policies"),
	url(r'^arch/$',
		views.Arch.as_view(),
		name="arch"),


]