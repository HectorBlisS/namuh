from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import SlideImg



class Home(View):
	def get(self,request):
		template_name='main/home.html'
		imgs=SlideImg.objects.all()
		context={
		'imgs':imgs
		}
		return render(request,template_name,context)

class Nosotros(TemplateView):
	template_name="main/us.html"

class Selling(TemplateView):
	template_name="main/selling.html"

class Policies(TemplateView):
	template_name="main/policies.html"

class Arch(TemplateView):
	template_name="main/arch.html"