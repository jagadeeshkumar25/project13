from django import  forms
from Hradmin.models import AdminModel,AddEmployeeModel



class AdminForm(forms.ModelForm):
    USERNAME=forms.CharField(max_length=30)
    PASSWORD= forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=AdminModel
        fields="__all__"


    def clean_USERNAME(self):
        name=self.cleaned_data['USERNAME']
        if len(name)>=4:
            return name
        else:
              raise forms.ValidationError("The minimum no of characters in the username field should be 4")

    def  clean_PASSWORD(self):
        password = self.cleaned_data['PASSWORD']
        if len(password)>=4:
            return password
        else:
            raise forms.ValidationError("minimun password must be 4 characters")


class AddEmployeeForm(forms.ModelForm):
    EMPLOYEENAME = forms.CharField()
    PASSWORD = forms.CharField(max_length=30,widget=forms.PasswordInput)
    CONTACTNO = forms.IntegerField()

    def clean_EMPLOYEENAME(self):
        name = self.cleaned_data['EMPLOYEENAME']
        if len(name) >= 4:
            return name
        else:
            raise forms.ValidationError("The minimum no of characters in the username field should be 4")

    def clean_PASSWORD(self):
        password = self.cleaned_data['PASSWORD']
        if len(password) >= 4:
            return password
        else:
            raise forms.ValidationError("minimun password must be 4 characters")

    def clean_CONTACTNO(self):
        con = self.cleaned_data['CONTACTNO']
        if len(str(con))==10:
            return con
        else:
            raise forms.ValidationError("contact must be 10 digits only ")

    class Meta:
        model=AddEmployeeModel
        fields="__all__"

