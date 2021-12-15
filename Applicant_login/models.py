from django.db import models
from Hradmin.models import AddEmployeeModel


class ApplicantModel(models.Model):
    USERNAME = models.CharField(max_length=30)
    PASSWORD = models.CharField(max_length=30)

class AddingDetailsModel(models.Model):
    ID=models.IntegerField(primary_key=True)
    NAME=models.CharField(max_length=30,unique=True)
    DATE_OF_BIRTH=models.DateField(help_text="yyyy-mm-dd")
    EMAIL=models.EmailField(max_length=30)
    GENDER=models.CharField(max_length=30)
    MOBILE=models.IntegerField()
    ADDRESS=models.CharField(max_length=30)
    USERNAME=models.CharField(max_length=30)
    PASSWORD=models.CharField(max_length=30)

class ApplicationModel(models.Model):
    ID = models.IntegerField(primary_key=True)
    NAME= models.CharField(max_length=30,unique=True)
    DATE_OF_BIRTH=models.DateField(help_text="yyyy-mm-dd")
    EMAIL=models.EmailField(max_length=30)
    GENDER=models.CharField(max_length=30)
    MOBILE=models.IntegerField()
    QUALIFICATION=models.CharField(max_length=30)
    POST = models.FloatField()
    PERCENTAGE=models.FloatField()
    RESUME = models.FileField(upload_to='applicant_document')

    # def __str__(self):
    #     return str(self.ID)

# class AddingDetailsModel(models.Model):
#     ID=models.IntegerField(primary_key=True)
#     NAME=models.CharField(max_length=30,unique=True)
#     DATE_OF_BIRTH=models.DateField(help_text="yyyy-mm-dd")
#     EMAIL=models.EmailField(max_length=30)
#     GENDER=models.CharField(max_length=30)
#     MOBILE=models.IntegerField()
#     ADDRESS=models.CharField(max_length=30)
#     USERNAME=models.CharField(max_length=30)
#     PASSWORD=models.CharField(max_length=30)
#
#     # def __str__(self):
#     #     return str(self.ID)
#     #

class InterviewModel(models.Model):
    Applicant_ID = models.IntegerField()
    employee_id = models.IntegerField()
    Schedule_Date=models.DateField(help_text="yyyy-mm-dd")


from django.db import models

# Create your models here.
