from django.contrib import admin

# Admin control for Contact
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact
        
admin.site.register(Contact, ContactAdmin)
