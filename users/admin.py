from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm

from .models import CustomUser
class CustomUserAdmin(UserAdmin):
    # Form to add in admin form
    add_form = CustomUserCreationForm

    form = CustomUserChangeForm
    # Fields to be displayed in admin form
    list_display = ['email', 'username']


admin.site.register(CustomUser, CustomUserAdmin)
