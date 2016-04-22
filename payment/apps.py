from __future__ import unicode_literals

from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'payment'
    verbose_name='Payment'

    def ready(self):
    	# import signals handlers
    	import payment.signals
