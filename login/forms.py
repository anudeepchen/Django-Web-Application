from django import forms
#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from .models import UserInformation
from django.contrib import messages
			
class UserInformationForm(forms.ModelForm):
	class Meta:
		model = UserInformation
		fields = '__all__'