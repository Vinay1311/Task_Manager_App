
from django.contrib import admin
from base_user.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email','is_active','is_admin_user']
    search_fields = ['id','email']
    list_filter = ['is_active','is_admin_user']