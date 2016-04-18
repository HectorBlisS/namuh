from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
	def __init__(self,request):
		"""
		Inicializamos el carrito
		"""
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			#Guardamos un carrito vacio en la sesión
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def add(self,product,quantity=1,update_quantity=False):
		"""
		Agregamos un producto al carro o lo actualizamos
		"""
		product_id = str(product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity':0,
			'price':str(product.price)}
		if update_quantity:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity
		self.save()

	def save(self):
		# actualizamos el carrito de la seision
		self.session[settings.CART_SESSION_ID] = self.cart
		# marcamos la sesion como modificada para asegurarnos de que se ha guardad
		self.session.modified = True

	def remove(self,product):
		"""
		Quitar un producto del carrito
		"""
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def __iter__(self):
		"""
		Iteramos en los objectos 
		del carrito y obtenemos los productos
		desde la base de Datos
		"""
		product_ids=self.cart.keys()
		# obtenemos los objetos y los agregamos al carrito
		products = Product.objects.filter(id__in = product_ids)
		for product in products:
			self.cart[str(product.id)]['product'] = product

		for item in self.cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item

	def __len__(self):
		"""
		Contar todos los elementos del carrito
		"""
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())

	def clear(self):
		# Remover el carrito de la sesion
		del self.session[settings.CART_SESSION_ID]
		self.session.modified=True




