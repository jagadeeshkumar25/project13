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

from HRhead import  views
urlpatterns = [

    path('hr_login_page/',views.HRLoginPage.as_view(),name="hr_login_page"),
    path('hr_home_page/',views.HRHomePage.as_view(),name="hr_home_page"),
    path('view_shortlisted/',views.ShortlisedApplicant.as_view(),name="view_shortlised"),
    path('selected_applicant/',views.SelectedApplicant.as_view(),name="selected_applicant"),
    path('rejected_applicant/', views.RejectedApplicant.as_view(), name="rejected_applicant")

]
