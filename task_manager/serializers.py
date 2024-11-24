#--------------- External Imports ----------------- #
from rest_framework import serializers

#--------------- Internal Imports ----------------- #
from task_manager.models import TaskData

# ------------------- Create Task Serializer------------------- #
class CreateTaskSerializer(serializers.ModelSerializer):
    """Serializer to create new tasks"""
    class Meta:
        model = TaskData
        fields = ['task_title', 'task_description', 'task_status']

# ------------------- Get Task Details Serializer------------------- #
class GetTaskDetailsSerializer(serializers.ModelSerializer):
    """Serializer to get Tasks details"""

    class Meta:
        model = TaskData
        fields = ['id', 'task_title', 'task_description', 'task_status']
        