from django.contrib import admin
from .models import Category,Product

# import export
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin

# para import export
class ProductResource(ModelResource):
	class Meta:
		model=Product

	def for_delete(self,row,instance):
		return self.fields['name'].clean(row) == ''

class CategoryAdmin(admin.ModelAdmin):
	list_display=['id','name','slug']
	prepopulated_fields={'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
	list_display=['id','name','slug','price','stock','available','created','updated']
	list_filter=['available','created','updated']
	list_editable=['price','stock','available']
	prepopulated_fields={'slug':('name',)}

# para import export
	resource_class=ProductResource

class CategoryAdmin(ExportActionModelAdmin):
	pass




admin.site.register(Product,ProductAdmin)
