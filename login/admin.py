from django.contrib import admin

# Register your models here.
from .models import FailedLogin,UserInformation


class FailedLoginAdmin(admin.ModelAdmin):
	list_display = ['email','ipaddr','timestamp']
	class Meta:
		model = FailedLogin
admin.site.register(FailedLogin,FailedLoginAdmin)


class UserInformationAdmin(admin.ModelAdmin):
	list_display = ['email','rgb','nvdi','timestamp']
	class Meta :
		model = UserInformation
admin.site.register(UserInformation,UserInformationAdmin)