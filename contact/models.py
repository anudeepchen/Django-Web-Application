from django.db import models
from django.core.validators import RegexValidator

# Contact model

class Contact(models.Model):
    # Attributes of the model
    first_name = models.CharField(max_length=120, null=False, blank=False, default="")
    last_name = models.CharField(max_length=120, null=False, blank=False, default="")
    email = models.EmailField(null=False, blank=False, default="")
    phone_regex = RegexValidator(regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
    phone = models.CharField(max_length=15, validators=[phone_regex], null = False, blank=False, default="")
    
    CLIENT = 'CL'
    INVESTOR = 'IN'
    PARTNER = 'PA'
    ACADEMIC = 'AC'
    OTHER = 'OT'
    INTEREST_CHOICES = (
        (CLIENT, 'Client'),
        (INVESTOR, 'Investor'),
        (PARTNER, 'Partner'),
        (ACADEMIC, 'Academic'),
        (OTHER, 'Other'),
    )
    interest = models.CharField(max_length=2, choices=INTEREST_CHOICES, default=CLIENT)

    message = models.TextField(max_length=250, null=False, blank=False, default="")
    
    def __str__(self):
        return self.email
