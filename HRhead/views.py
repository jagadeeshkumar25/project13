from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.views.generic import View
from.models import HRModel
from.form import HRForm
from Applicant_login .models import ApplicationModel
from Interviwer .models import InterviewApplicantModel


class HRLoginPage(View):
    def get(self,request):
        return  render(request,"HRHead/hr-login-page.html",{"Hff":HRForm()})


class HRHomePage(View):
    def post(self,request):
        return  render(request,"HRHead/hr_home_page.html")


class ShortlisedApplicant(View):
    def get(self,request):
        ap=ApplicationModel.objects.all()
        return  render(request,"HRHead/all_shortlised_appicant.html",{"data":ap})


class SelectedApplicant(View):
    def get(self,request):
        im=InterviewApplicantModel.objects.all()
        return  render(request,"HRHead/selected_applicant.html",{"data":im})


class RejectedApplicant(View):
    def get(self,request):
        im=InterviewApplicantModel.objects.all()
        return  render(request,"HRHead/rejected_applicant.html",{"data":im})
