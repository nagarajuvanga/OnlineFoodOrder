from django import forms
from pwn.models import StateModel

class StateForm(forms.ModelForm):
    class Meta:
        model=StateModel
        fields="__all__"