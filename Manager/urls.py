"""realtimeproject1_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django .views.generic.base import TemplateView
from Hradmin import urls as admin
from Manager import views





urlpatterns = [
     path('manager_login_page/',views.ManagerLogin.as_view(),name="manager_login_page"),
    path('manager_home_page/',views.ManagerHome.as_view(),name="manager_home_page"),
    path('recuirtment_page/',views.Recuirtment.as_view(),name="recuirtment_page"),
    path('adding_details/',views.RecuirtmentDetails.as_view(),name="adding_details"),
    path('modify/',views.Modify.as_view(),name="modify"),
    path('update_details/',views.UpdateDetails.as_view(),name="update_details"),
    path('delete_details/',views.DEleteDetails.as_view(),name="delete_details"),
    # path('interview/',views.InterviewSchedule.as_view(),name="interview")



]
