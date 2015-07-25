from django.contrib import admin
from .models import Document
# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
	list_display = ['url','timestamp']
	class Meta:
		model = Document
admin.site.register(Document,DocumentAdmin)