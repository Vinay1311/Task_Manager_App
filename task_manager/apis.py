#---------- External Imports
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import threading

#---------- Internal Imports
from base_user.models import User
from helper import keys, messages
from helper.status import *
from helper.functions import send_registration_email
from task_manager.models import TaskData, SendRegisterationEmailData
from task_manager.serializers import CreateTaskSerializer, GetTaskDetailsSerializer

# ------------------ Post Api To Create a new task ------------------ #
class CreateTaskApi(generics.CreateAPIView):
    """
    Api to create a new task with details
    """

    serializer_class  = CreateTaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes= [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = self.get_serializer(data = data)
        if not serializer.is_valid():
            errors = serializer.errors
            return Response({keys.ERROR: errors}, status=status400)
        
        serializer.save()
        return Response({keys.MESSAGE: messages.TASK_CREATED}, status=status201)
    
# ------------------ Get Api to get a task or list of all tasks------------------ #
class GetTaskDetailsApi(generics.GenericAPIView):
    """
    Api to get a task with details or all tasks with details
    """

    serializer_class  = GetTaskDetailsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes= [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        task_id = self.request.GET.get(keys.TASK_ID)

        user_instance = request.user

        if task_id:
            task_instance = TaskData.objects.filter(id = task_id)
            if task_instance.exists():
                task_instance = task_instance.first()
                serializer = self.get_serializer(task_instance)
            else:
                return Response({keys.ERROR: messages.TASK_NOT_FOUND}, status=status404)
            
        else:
            task_instance = TaskData.objects.filter(user = user_instance)
            serializer = self.get_serializer(task_instance, many=True)

        return Response(({keys.MESSAGE: messages.TASK_DETAILS_FETCHED, 'data':serializer.data}, serializer.data), status=status201)
    
# ------------------ Post Api to update a task ------------------ #
class UpdateTaksDetailsApi(generics.GenericAPIView):
    """
    Api to update a task details
    """

    serializer_class  = CreateTaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes= [JWTAuthentication]

    def patch(self, request, *args, **kwargs):
        task_id = self.request.GET.get(keys.TASK_ID)
        data = request.data.copy()

        data['user'] = request.user.id

        if task_id:
            task_instance = TaskData.objects.get(id = task_id)

            serializer = self.get_serializer(instance=task_instance, data = data, partial = True)
            if not serializer.is_valid():
                errors = serializer.errors
                return Response({keys.ERROR: errors}, status=status400)
            
            serializer.save()
            return Response({keys.MESSAGE: messages.TASK_DETAILS_UPDATED}, status=status200)

        else:
            return Response({keys.ERROR: messages.TASK_NOT_FOUND}, status=status400)

# ------------------ Post Api to delete a task ------------------ #
class DeleteTaskApi(generics.GenericAPIView):
    """
    Api to delete task 
    """

    def delete(self, request, *args, **kwargs):
        task_id = self.request.GET.get(keys.TASK_ID)

        if task_id:
            task_instance = TaskData.objects.get(id = task_id)
            task_instance.delete()
            return Response({keys.MESSAGE: messages.TASK_DETAILS_DELETED}, status=status201)
        else:
            return Response({keys.ERROR: messages.TASK_NOT_FOUND}, status=status400)
        

# ------------------ Post Api to sent email to user with link registration ------------------ #
class SentRegistrationEmailApi(generics.GenericAPIView):
    """
    Api to sent the new user the registation email from api if is the admin user.
    """

    def post(self, request, *args, **kwargs):
        user_name = request.data[keys.USER_NAME]
        email = request.data[keys.EMAIL]

        user_id = request.user.id
        user_instance = User.objects.get(id = user_id)
    
        if user_instance.is_admin_user == True:
            try:
                sent_registration_email_instance, created = SendRegisterationEmailData.objects.get_or_create(user_name = user_name, email = email)
                return Response({keys.MESSAGE: messages.EMAIL_SENT_SUCCESSFULLY}, status=status200)
            except Exception as e:
                return Response({keys.ERROR: {str(e)}}, status=status400)
        else:
            return Response({keys.ERROR: messages.NOT_HAVE_ACCESS}, status=status400)
