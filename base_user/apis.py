#---------- External Imports
from rest_framework import generics
from rest_framework.response import Response
#---------- Internal Imports
from helper import keys, messages
from helper.status import *
from helper.functions import get_tokens_for_user
from base_user.models import User

# ------------------ Post Api To Create User Instance, login & get Token ------------------ #
class CreateUserLoginApi(generics.GenericAPIView):
    """
    Api to Create user instance, login and get token
    """

    def post(self, request, *args, **kwargs):
        try:
            email = request.data.get(keys.EMAIL)

            if not email:
                return Response({keys.ERROR: messages.EMAIL_REQUIRED}, status=status400)
            
            user_instance, created = User.objects.get_or_create(email = email)

            token = get_tokens_for_user(user_instance)

            return Response({keys.MESSAGE: messages.LOGIN_SUCCESSFULLY, "token":token}, status200)
        
        except Exception as e:
            return Response({keys.ERROR: str(e)}, status500)
