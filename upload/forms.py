from django import forms
from .models import Document
from django.contrib import messages
	
class DocumentForm(forms.Form):
	docfile = forms.ImageField(label='Select a file', help_text='max. 42 megabytes')
	class Meta:
		model = Document
		fields ='__all__'