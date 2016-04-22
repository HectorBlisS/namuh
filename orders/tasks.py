# -*- coding: utf-8 -*-
from celery import task
from django.core.mail import send_mail
from .models import Order



@task
def order_created(order_id):
	"""
	Tarea para enviar una notificacion 
	email cuando una orden es creada
	"""
	order=Order.objects.get(id=order_id)
	subject='Orden #{}'.format(order.id)
	message='Estimado {},\n\nTu orden ha sido correctamente recibida El id de tu orden es: {}.'.format(order.first_name,order_id)
	mail_sent=send_mail(subject,message,'contacto@fixter.org',[order.email])
	return mail_sent