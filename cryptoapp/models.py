from django.db import models

# Create your models here.
class Account_Details(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    Email = models.EmailField(max_length=50,  blank=True)
    
class Change_password(models.Model):
    Old_password = models.CharField(max_length=30, blank=True)
    New_password = models.CharField(max_length=30, blank=True)
    Confirm_new_password = models.CharField(max_length=30, blank=True)
