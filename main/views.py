from django.shortcuts import render
from django.views.generic import View
from .models import SlideImg



class Home(View):
	def get(self,request):
		template_name='main/home.html'
		imgs=SlideImg.objects.all()
		context={
		'imgs':imgs
		}
		return render(request,template_name,context)
