from django.contrib import admin
from .models import UserData

# Register your models here.


class UserFormAdd(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'email_id','password')


admin.site.register(UserData,UserFormAdd)  # For View Purpose only
