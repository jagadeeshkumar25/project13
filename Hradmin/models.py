from django.db import models

# Create your models here.


from django.db import models

class AdminModel(models.Model):
    USERNAME = models.CharField(max_length=30,unique=True)
    PASSWORD = models.CharField(max_length=30)



class AddEmployeeModel(models.Model):
    des =(
        ('MANAGER','MANAGER'),
        ('HRHEAD','HRHEAD'),
        ('INTERVIWER','INTERVIWER'),
        ('EMPLOYEE','EMPLOYEE')
    )

    EMPLOYEENAME =  models.CharField(max_length=30, unique=True)
    PASSWORD     =  models.CharField(max_length=30)
    DESIGNATION  =  models.CharField(max_length=30,choices=des)
    ADDRESS      =  models.CharField(max_length=50)
    CONTACTNO    =  models.IntegerField()
    EMAIL        =  models.EmailField()

