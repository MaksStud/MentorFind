from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'email')
    search_fields = ('email', )

