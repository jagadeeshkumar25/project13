from django.db import models

class Interviewer_LoginModel(models.Model):
    USERNAME=models.CharField(max_length=30)
    PASSWORD=models.CharField(max_length=30)



class InterviewApplicantModel(models.Model):
    # re=(
    #     ("SELECTED","SELECTED"),
    #     ("REJECTED","REJECTED")
    # )
    Interview_ID=models.IntegerField()
    Interviewer=models.IntegerField()
    SCHEDULE_TIMESTAMP=models.DateField(help_text="yyyy-mm-dd")
    Applicant_id=models.IntegerField()
    Result=models.CharField(max_length=30)
from django.db import models

# Create your models here.
