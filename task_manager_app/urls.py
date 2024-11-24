"""
URL configuration for task_manager_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("base_user/", include('base_user.urls')), #URL Path for base_user app
    path("task_manager/", include('task_manager.urls')), #URL Path for base_user app

    path('accounts/', include('allauth.urls')), #all OAuth operations will be performed under this route
    path('logout', LogoutView.as_view()) #default Django logout view at /logout
]
