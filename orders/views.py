from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.views.generic import View



class OrderCreate(View):
	def get(sefl,request):
		cart=Cart(request)
		form=OrderCreateForm()
		template='orders/order/create.html'
		context={
		'cart':cart,
		'form':form
		}
		return render(request,template,context)

	def post(self,request):
		cart=Cart(request)
		form=OrderCreateForm(request.POST)
		if form.is_valid():
			order=form.save()
			for item in cart:
				OrderItem.objects.create(order=order,
					product=item['product'],
					price=item['price'],
					quantity=item['quantity'])
			# Borrar el carrito
			cart.clear()
			template='orders/order/created.html'
			context={
			'order':order
			}
			return render(request,template,context)



