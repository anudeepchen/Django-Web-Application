from django.db import models

# Create your models here.
class Document(models.Model):
    #docfile = models.FileField(blank = True, null=True, upload_to='media/')
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False,null =True)
    url = models.CharField(max_length=128,null=True)
    def _str_(self):
        return self.docfile