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
from django.urls import path
from django .views.generic.base import TemplateView
from Applicant_login import views
from django.conf.urls.static import static




urlpatterns = [
    path('applicant_login_page/',views.ApplicantLoginPage.as_view(),name="applicant_login_page"),
    path('register/',views.ApplicantRegistration.as_view(),name="register"),
    path('application/',views.ApplicationForm1.as_view(),name="application"),
    path('submitform/',views.ApplicationForm2.as_view(),name="submitform"),
    path('interview/', views.InterviewSchedule.as_view(), name="interview"),
    path('interviewschedule/',views.InterviewSchedule1.as_view(),name="interviewschedule")

]

