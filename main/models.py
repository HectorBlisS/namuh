from django.db import models



class SlideImg(models.Model):
	img=models.ImageField(upload_to='slides_img')
	url=models.URLField(max_length=200,blank=True,null=True)
	name=models.CharField(max_length=100,null=True,blank=True)
	
	def __str__(self):
		return self.name
