from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import  UserAdmin
from .forms import  CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form  = CustomUserChangeForm
    model = CustomUser
    #list_display = ['first_name','username', 'email', 'last_name','username', 'is_staff','is_active',]
    list_display = ['username', 'email',]


admin.site.register(CustomUser, CustomUserAdmin)