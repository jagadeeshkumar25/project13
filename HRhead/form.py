from django import forms
from.models import HRModel


class HRForm(forms.ModelForm):
    USERNAME=forms.CharField(max_length=30)
    PASSWORD=forms.CharField(widget=forms.PasswordInput,max_length=30)

    class Meta:
        model=HRModel
        fields="__all__"