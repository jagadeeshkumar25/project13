from django.db import models

from Applicant_login.models import ApplicationModel
from Hradmin.models import AddEmployeeModel


class ManagerModel(models.Model):
    USERNAME= models.CharField(max_length=30)
    PASSWORD = models.CharField(max_length=30)


class AddingDetails(models.Model):
    OPPERTUNITY_CODE         =   models.IntegerField(primary_key=True)
    QUALIFICATION            =   models.CharField(max_length=50)
    RESISTARTION_START_FORM   =  models.DateTimeField(blank=True,null=True)
    AGE_LIMIT                 =   models.IntegerField()
    LAST_DAY_TO_APPLY         =  models.DateTimeField(blank=True,null=True)
    DEPARTMENT_ID             =   models.CharField(max_length=50)
    NO_OF_POSITION            =   models.IntegerField()
    DESCRIPTION               =  models.CharField(max_length=50)
    RESPONSIBILITIES          =  models.CharField(max_length=50)
    CONTACTNO                 =  models.IntegerField()


# class ManagerInterviewModel(models.Model):
#     Applicant_ID = models.OneToOneField(ApplicationModel,on_delete=models.CASCADE)
#     employee_id = models.OneToOneField(AddEmployeeModel,on_delete=models.CASCADE,primary_key=True)
#     Schedule_Date=models.DateField(help_text="yyyy-mm-dd")
#


