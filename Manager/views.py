from django.contrib import messages
from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic.base import View
from.models import ManagerModel,AddingDetails
from.form import ManagerForm,AddingDetailsForm


class ManagerLogin(View):
    def get(self, request):
        return render(request,"Manager/manager.html",{"ml":ManagerForm()})


    def post(self, request):
        USERNAME = request.POST['u1']
        PASSWORD = request.POST['p1']
        if USERNAME == "manager" and PASSWORD == "manager":
            return redirect('manager_home_page')
        else:
            mess = "please check username and password"
            messages.success(request, mess)
            return render(request, "Manager/manager.html")




class ManagerHome(View):
    def post(self,request):
        return render(request,"Manager/manager_home_page.html")



class Recuirtment(View):
    def get(self,request):
        return render(request,"Manager/recuirtment.html")



class RecuirtmentDetails(View):
    def get(self, request):
        all_d = AddingDetails.objects.all()
        return render(request, "Manager/recuirtment_details.html", {"af": AddingDetailsForm(), "all_d": all_d})



    def post(self, request):
        add = request.POST["a2"]
        if add == "add":
            rf = AddingDetailsForm(request.POST)
            if rf.is_valid():
                rf.save()
                mess = "Details are saved in database"
                messages.success(request, mess)
                return redirect('adding_details')
            else:
                print('wrong')
                return render(request, "manager/recuirtment_details.html", {"af": AddingDetailsForm})


class Modify(View):
    def get(self,request):
       qs= AddingDetails.objects.all()
       return render(request,"Manager/modify.html",{"data":qs})
    def post(self,request):
        id=request.POST['t1']
        # qu=request.POST["e1"]
        # reg=request.POST["e3"]
        # age=request.POST["e4"]
        # last=request.POST["e5"]
        # did=request.POST["e6"]
        # no=request.POST["e7"]
        # des=request.POST["e8"]
        # resp=request.POST["e9"]
        # con=request.POST["10"]

        qs=AddingDetails.objects.get(OPPERTUNITY_CODE=id)

        return  render(request,"manager/modify_page.html",{"data":qs,"af":AddingDetailsForm})


class UpdateDetails(View):
    def post(self,request):
         qu=request.POST["e1"]
         reg=request.POST["e3"]
         age=request.POST["e4"]
         last=request.POST["e5"]
         did=request.POST["e6"]
         no=request.POST["e7"]
         des=request.POST["e8"]
         resp=request.POST["e9"]
         con=request.POST["e10"]

         qs=AddingDetails.objects.update(QUALIFICATION=qu,RESISTARTION_START_FORM=reg,AGE_LIMIT=age,LAST_DAY_TO_APPLY=last,DEPARTMENT_ID=did,NO_OF_POSITION=no, DESCRIPTION=des,RESPONSIBILITIES=resp,CONTACTNO=con)


         return redirect('modify')


class DEleteDetails(View):
        def get(self, request):
            qs = AddingDetails.objects.all()
            return render(request, "manager/delete.html", {"data": qs})

        def post(self, request):
            check = request.POST.getlist("c1")
            for x in check:
                AddingDetails.objects.filter(OPPERTUNITY_CODE=x).delete()
            return redirect('delete_details')

