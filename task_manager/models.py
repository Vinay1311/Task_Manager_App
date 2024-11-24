#---------- External Imports
from django.db import models
import uuid
#---------- Internal Imports
from helper import keys
from base_user.models import User

# --------------- Task Data Model
class TaskData(models.Model):
    """ Tasks Data Model to store deatils of the tasks"""
    id = models.UUIDField(primary_key=True, editable=False, default = uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_task_model')
    task_title = models.CharField(max_length=250)
    task_description = models.TextField()
    task_status = models.CharField(max_length=50, choices=[('completed', 'Completd'), ('incompleted', 'Incompletd')], default='incompleted')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}-{self.task_title}"


# --------------- Send Registration Email Data model
class SendRegisterationEmailData(models.Model):
    """ Send Resisteration Email Model to store the & share the new user registration email """
    id = models.UUIDField(primary_key=True, editable=False, default = uuid.uuid4)
    user_name = models.CharField(max_length=250)
    email = models.EmailField()
    flag_email_sent = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email}"
