from django.urls import path
from task_manager.apis import *

urlpatterns = [
    #Get API
    path('get-task-details/', GetTaskDetailsApi.as_view()), #URL Path to get task details
    
    #Post API
    path('add-task-details/', CreateTaskApi.as_view()), #URL Path to create/add task details 
    path('update-task-details/', UpdateTaksDetailsApi.as_view()), #URL Path to update task details
    path('send-registration-email/', SentRegistrationEmailApi.as_view()), #URL Path to send redistration email if user is admin user
    
    #Delete API
    path('delete-task-details/', DeleteTaskApi.as_view()), #URL Path to delete tasks
    
]