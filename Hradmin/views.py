from django.contrib import messages
from django.shortcuts import render,redirect
from.models import AddEmployeeModel,AdminModel
from.form import AddEmployeeForm,AdminForm

# Create your views here.
from django.views.generic.base import View


class AdminLogin(View):
    def get(self, request):
        return render(request, "HRadmin/admin_login.html")

    def post(self, request):
        USERNAME = request.POST['u1']
        PASSWORD = request.POST['p1']
        if USERNAME == "admin" and PASSWORD == "admin":
            print("hi")
            return redirect('admin_home_page')
        else:
            mess = "please check username and password"
            messages.success(request, mess)
            print("hello")
            return render(request, "HRadmin/admin_login.html")


class AdminHome(View):
    def get(self, request):
        return render(request, "HRadmin/admin_home.html")


class AddEmployee(View):
    def get(self,request):
        all_d=AddEmployeeModel.objects.all()
        return render(request,"HRadmin/add_employee.html",{"ae":AddEmployeeForm(),"all_d":all_d})

    def post(self,request):
        add_details=request.POST["a1"]
        if add_details=="add_details":
            add_details=AddEmployeeForm(request.POST)
            if add_details.is_valid():
                add_details.save()
                mess= "Details are saved in database"
                messages.success(request,mess)
                return redirect('add_employee_page')
            else:
                return render(request, "HRadmin/add_employee.html", {"ae": AddEmployeeForm})




class ViewEmployeeDetails(View):
    def get(self,request):
     qs=AddEmployeeModel.objects.all()
     return render(request,"HRadmin/view_employee_details.html",{"data":qs})



class UpdateEmployee(View):
    def get(self, request):
        qs = AddEmployeeModel.objects.all()
        return render(request, "HRadmin/update.html", {"data": qs})


class UpdateEmployeeDetails(View):
    def get(self, request):
        id = request.GET["empid"]
        r = AddEmployeeModel.objects.get(id=id)
        return render(request, "HRadmin/update_employee.html", {"data": r})

    def post(self, request):
        name = request.POST["e1"]
        idno = request.POST["e2"]
        des = request.POST["e3"]
        ad = request.POST["e4"]
        con = request.POST["e5"]
        em = request.POST["e6"]
        res = AddEmployeeModel.objects.filter(id=idno)
        res.update(EMPLOYEENAME=name, DESIGNATION=des, ADDRESS=ad, CONTACTNO=con, EMAIL=em)
        return redirect('view_employee_details')


class Delete(View):
    def get(self, request):
        qs = AddEmployeeModel.objects.all()
        return render(request, "HRadmin/delete.html", {"data": qs})

    def post(self, request):
        check = request.POST.getlist("c1")
        for x in check:
            AddEmployeeModel.objects.filter(id=x).delete()
        return redirect('view_employee_details')
