from django.conf.urls import url
from . import views



urlpatterns=[
	url(r'^$',
		views.CartDetail.as_view(),
		name="cart_detail"),

	url(r'^add/(?P<product_id>\d+)/$',
		views.CartAdd.as_view(),
		name="cart_add"),

	url(r'^remove/(?P<product_id>\d+)/$',
		views.CartRemove.as_view(),
		name="cart_remove"),
]