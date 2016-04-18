from django.shortcuts import render, get_object_or_404
from .models import Category,Product
from django.views.generic import View

from cart.forms import CartAddProductForm



class ProductListView(View):
	def get(self,request,category_slug=None):
		category=None
		categories=Category.objects.all()
		products=Product.objects.filter(available=True)
		if category_slug:
			category=get_object_or_404(Category,slug=category_slug)
			products=products.filter(category=category)
		template='shop/product/list.html'
		context={
		'category':category,
		'categories':categories,
		'products':products
		}
		return render(request,template,context)	

class ProductDetailView(View):
	def get(self,request,id,slug):
		product=get_object_or_404(Product,id=id,slug=slug,available=True)
		template='shop/product/detail.html'
		cart_product_form=CartAddProductForm()
		context={
		'product':product,
		'cart_product_form':cart_product_form,
		}
		return render(request,template,context)
