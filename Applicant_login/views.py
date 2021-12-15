from django.shortcuts import render,redirect
from django.views.generic import View
from.form import ApplicantForm,AddingDetailsForm,ApplicationForm
from django.contrib import messages
from.models import ApplicationModel,AddingDetailsModel,InterviewModel
from Hradmin.models import AddEmployeeModel

class ApplicantLoginPage(View):
    def get(self,request):
        return render(request,"applicant/applicant_login_page.html",{"af":ApplicantForm()})

class ApplicantRegistration(View):
    def get(self, request):
        return render(request, "applicant/applicant_registration_form.html", {"ad": AddingDetailsForm()})

    def post(self,request):
        register=request.POST["r1"]
        print("hello")
        if register=="register":
            print("jagad")
            register= AddingDetailsForm(request.POST)
            print("madhu")
            if register.is_valid():
               print('hi')
               register.save()
               msg="Details are saved in databasse"
               messages.success(request,msg)
               return render(request, "applicant/applicant_registration_form.html", {"ad": AddingDetailsForm})
            else:
                 print('bye')
            return render(request, "applicant/applicant_registration_form.html", {"ad": AddingDetailsForm})


class ApplicationForm1(View):
    def post(self,request):
        return render(request,"applicant/applicationform.html",{"aff":ApplicationForm()})

class ApplicationForm2(View):
    def post(self, request):
        apply = request.POST["a1"]
        if apply == "apply":
            print("hii")
            apply = ApplicationForm(request.POST,request.FILES)
            if apply.is_valid():
                print("hello")
                apply.save()
                msg = "Details are saved in databasse"
                messages.success(request, msg)
                return render(request, "applicant/applicationform.html", {"aff": ApplicationForm})
            else:
                print("byee")
            return render(request, "applicant/applicationform.html", {"aff": ApplicationForm})


class InterviewSchedule(View):
    def get(self,request):
        return render(request,"applicant/interview.html",{"data":ApplicationModel.objects.all()})
    def post(self,request):
        id=request.POST["t1"]
        qs=ApplicationModel.objects.get(ID=id)
        return  render(request,"applicant/interview_page.html",{"data":qs,"data1":AddEmployeeModel.objects.all()})


class InterviewSchedule1(View):
    def post(self,request):
        id1=request.POST['i1']
        emp1=request.POST['i2']
        sc=request.POST['i3']
        im=InterviewModel(Applicant_ID=id1,employee_id=emp1,Schedule_Date=sc)
        im.save()
        return render(request,"applicant/interview_page.html",{"message":"Details are  saved"})


from django.shortcuts import render

# Create your views here.
