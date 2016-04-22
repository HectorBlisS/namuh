from django.shortcuts import render, get_object_or_404
from .models import Category,Product
from django.views.generic import View, ListView

from cart.forms import CartAddProductForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ProductListView(View):
	def get(self,request,category_slug=None):
		category=None
		categories=Category.objects.all()
		products=Product.objects.filter(available=True)
		if category_slug:
			category=get_object_or_404(Category,slug=category_slug)
			products=products.filter(category=category)
		paginator=Paginator(products,12)
		page=request.GET.get('page')
		try:
			prods=paginator.page(page)
		except PageNotAnInteger:
			prods=paginator.page(1)
		except EmptyPage:
			prods=paginator.page(paginator.num_pages)
		template='shop/product/list.html'
		context={
		'category':category,
		'categories':categories,
		'products':prods,
		'page':page
		}
		return render(request,template,context)	

# class ProductList(ListView):

# 	def get_queryset(self):
# 		self.category_slug=self.kwargs['category_slug']
# 		if self.category_slug:
# 			self.category=get_object_or_404(Category, slug=self.category_slug)
# 			return Product.objects.filter(category=self.category)
# 		else:
# 			return Product.objects.filter(available=True)
	
# 	context_object_name="products"
# 	paginate_by=12
# 	template_name='shop/product/list.html'

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
