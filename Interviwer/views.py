from django.shortcuts import render

from django.shortcuts import render
from django.views.generic.base import View
from.models import Interviewer_LoginModel,InterviewApplicantModel
from.form import Interview_loginForm
from Applicant_login.models import ApplicationModel
from Interviwer.form import InterviewApplicantForm
from Applicant_login.form import AddingDetailsForm


class InterviwererLoginPage(View):
    def get(self,request):
        return render(request,"Interviwer/Interviewer_login_page.html",{"If":Interview_loginForm()})


class FinalSelectionPage(View):
    def post(self,request):
        return render(request,"Interviwer/interviewer.html",{"data":ApplicationModel.objects.all()})


class InterviewApplicant(View):
    def post(self,request):
        id=request.POST["t1"]
        qs = ApplicationModel.objects.get(ID=id)
        return render(request, "Interviwer/interview_page.html", {"data": qs,"data1":InterviewApplicantModel})


class InterviewApplicant1(View):
    def post(self,request):
        interview_id=request.POST['i1']
        interviewer=request.POST['i2']
        schedule_time=request.POST['i3']
        applicant_id=request.POST['i4']
        result=request.POST['i5']
        im=InterviewApplicantModel(Interview_ID=interview_id,Interviewer=interviewer,
                                   SCHEDULE_TIMESTAMP=schedule_time,Applicant_id=applicant_id,Result=result)
        im.save()
        return render(request,"Interviwer/interview_page.html",{"message":"Details are saved in database"})
