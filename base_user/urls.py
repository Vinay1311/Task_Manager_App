from django.urls import path
from base_user.apis import *

urlpatterns = [
    #Post API
    path('user-login/', CreateUserLoginApi.as_view()), #URL Path to creaet User , Login & generate token 
]