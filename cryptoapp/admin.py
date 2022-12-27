from django.contrib import admin
from .models import *

# Register your models here.
class Account_DetailsAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone', 'Email')
admin.site.register(Account_Details, Account_DetailsAdmin)

class Change_passwordAdmin(admin.ModelAdmin):
    list_display = ('New_password','Confirm_new_password')
admin.site.register(Change_password, Change_passwordAdmin)

# Register your models here.
