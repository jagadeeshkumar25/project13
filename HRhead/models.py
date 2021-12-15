from django.db import models

# Create your models here.


from django.db import models


class HRModel(models.Model):
    USERNAME=models.CharField(max_length=30)
    PASSWORD=models.CharField(max_length=30)