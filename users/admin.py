from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("id", 'email')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_staff', 'is_active', 'birthdate')}),
        ('Personal info', {'fields': ('username',)}),
        ('Date information', {'fields': ('last_login',)}),
    )

    