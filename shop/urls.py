from django.conf.urls import url
from . import views



urlpatterns=[
	url(r'^$',
		views.ProductListView.as_view(),
		name='product_list'),

	url(r'^(?P<category_slug>[-\w]+)/$',
		views.ProductListView.as_view(),
		name='product_list_by_category'),

	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
		views.ProductDetailView.as_view(),
		name='product_detail'),
]