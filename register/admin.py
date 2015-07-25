from django.contrib import admin
from .models import Register

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','email','phone','password','timestamp','updated','acc_locked']
	class Meta:
		model = Register
admin.site.register(Register,RegisterAdmin)