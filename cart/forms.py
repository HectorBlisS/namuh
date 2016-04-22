from django import forms



PRODUCT_QUARNTITY_CHOICES = [(i,str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):
	quantity=forms.TypedChoiceField(label="Cantidad",choices=PRODUCT_QUARNTITY_CHOICES,coerce=int)
	update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
	