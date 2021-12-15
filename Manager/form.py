from django import forms
from Manager.models import ManagerModel,AddingDetails


class ManagerForm(forms.ModelForm):
    USERNAME= forms.CharField(max_length=30)
    PASSWORD= forms.CharField(widget=forms.PasswordInput,max_length=30)
    class Meta:
        model= ManagerModel

        fields= "__all__"


class AddingDetailsForm(forms.ModelForm):
    OPPERTUNITY_CODE = forms.IntegerField()
    QUALIFICATION = forms.CharField(max_length=50)
    AGE_LIMIT = forms.IntegerField()
    DEPARTMENT_ID = forms.CharField(max_length=50)
    NO_OF_POSITION = forms.IntegerField()
    DESCRIPTION = forms.CharField(max_length=50)
    RESPONSIBILITIES = forms.CharField(max_length=50)
    CONTACTNO = forms.IntegerField()
    RESISTARTION_START_FORM = forms.DateTimeField(help_text="yyyy-mm-dd")
    LAST_DAY_TO_APPLY = forms.DateTimeField(help_text="yyyy-mm-dd")
    class Meta:
        model= AddingDetails
        fields="__all__"


