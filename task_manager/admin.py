from django.contrib import admin
from task_manager.models import TaskData, SendRegisterationEmailData

@admin.register(TaskData)
class TaskDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_title', 'task_description','task_status']
    search_fields = ['id', 'task_title', 'task_description']
    list_filter = ['task_status']
    readonly_fields = ['created_at','updated_at']

@admin.register(SendRegisterationEmailData)
class SendRegisterationEmailDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'email','flag_email_sent']
    search_fields = ['id', 'user_name', 'email']
    list_filter = ['flag_email_sent']
    readonly_fields = ['created_at','updated_at']
