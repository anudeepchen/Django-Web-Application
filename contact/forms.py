from django import forms
from .models import Contact
from nocaptcha_recaptcha.fields import NoReCaptchaField

class ContactForm(forms.ModelForm):
    # Initiate the placeholder and id for all fields
    def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
            self.fields['email'].widget.attrs['placeholder'] = 'Email'
            self.fields['phone'].widget.attrs['placeholder'] = 'Phone number'
            self.fields['message'].widget.attrs['placeholder'] = 'Please input your message here'
    
    class Meta:
        model = Contact
        fields = '__all__'
        
    captcha = NoReCaptchaField(gtag_attrs={'data-theme':'dark'})