from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
  
    
class FailedLogin(models.Model):
    email = models.EmailField(null=False, blank=False, default="")
    ipaddr = models.CharField(max_length=30, null=False, blank=False, default="")
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)

    def _str_(self):
        return self.user
    
class UserInformation(models.Model):
    email = models.EmailField(null=False, blank=False, default="")
    rgb = models.BooleanField()
    nvdi = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False,null =True)