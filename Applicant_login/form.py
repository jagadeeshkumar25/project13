from django import forms
from.models import ApplicantModel,AddingDetailsModel,ApplicationModel

class ApplicantForm(forms.ModelForm):
    USERNAME= forms.CharField(max_length=30)
    PASSWORD= forms.CharField(widget=forms.PasswordInput,max_length=30)
    class Meta:
        model= ApplicantModel

        fields= "__all__"


class AddingDetailsForm(forms.ModelForm):
    ge=(
        ('male','male'),
        ('female','female'),
        ('others','others')
    )
    ID=forms.IntegerField(min_value=1)
    NAME=forms.CharField()
    DATE_OF_BIRTH=forms.DateField(help_text="yyyy-mm-dd")
    EMAIL=forms.EmailField()
   # GENDER=forms.CharField(widget=forms.RadioSelect(choices=ge))
    GENDER=forms.CharField(widget=forms.Select(choices=ge))
    MOBILE=forms.IntegerField()
    ADDRESS=forms.CharField()
    USERNAME=forms.CharField()
    PASSWORD=forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model=AddingDetailsModel
        fields="__all__"

class ApplicationForm(forms.ModelForm):
    ge = (
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others')
    )
    po=(
        (1,1),(2,2),(3,3),('above 5 years','above 5 years')
    )
    ID = forms.IntegerField()
    NAME= forms.CharField(max_length=30)
    DATE_OF_BIRTH=forms.DateField(help_text="yyyy-mm-dd")
    EMAIL=forms.EmailField(max_length=30)
    GENDER=forms.CharField(widget=forms.RadioSelect(choices=ge))
    MOBILE=forms.IntegerField()
    QUALIFICATION=forms.CharField(max_length=30)
    POST = forms.ChoiceField(choices=po)
    PERCENTAGE=forms.FloatField()

    class Meta:
        model=ApplicationModel
        fields="__all__"



