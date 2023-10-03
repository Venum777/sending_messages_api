from django.contrib import admin
from .models import MyCustomUser

@admin.register(MyCustomUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number']
    list_filter = ['username', 'email', 'phone_number']