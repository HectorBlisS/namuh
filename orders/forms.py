#-*-encoding: utf-8 -*-
from django import forms
from .models import Order
from django.utils.translation import ugettext_lazy as _


my_default_errors = {
    'required': 'Este campo es necesario',
    'invalid': 'Introduzca un dato valido'
}


class OrderCreateForm(forms.ModelForm):
	class Meta:
		model=Order
		fields=['first_name',
		'last_name',
		'email',
		'address',
		'postal_code',
		'city']
		labels={
		'first_name':_('Tu nombre'),
		'last_name':_('Apellido'),
		'address':_('Direccion'),
		'postal_code':_('Codigo postal'),
		'city':_('Ciudad')
		}
		error_messages = {
			'first_name': my_default_errors,
			'last_name': my_default_errors,
			'email': my_default_errors,
			'address': my_default_errors,
			'postal_code': my_default_errors,
			'city': my_default_errors
		}
		