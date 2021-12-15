from django import forms
from.models import Interviewer_LoginModel,InterviewApplicantModel


class Interview_loginForm(forms.ModelForm):
    USERNAME=forms.CharField(max_length=30)
    PASSWORD=forms.CharField(widget=forms.PasswordInput,max_length=30)

    class Meta:
        model=Interviewer_LoginModel
        fields="__all__"



class InterviewApplicantForm(forms.ModelForm):
    # re = (
    #     ("SELECTED", "SELECTED"),
    #     ("REJECTED", "REJECTED")
    # )
    # Result=forms.CharField(max_length=30,widget=forms.Select(choices=re))

    class Meta:
        model = InterviewApplicantModel
        fields = "__all__"


