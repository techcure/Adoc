from django import forms

from .models import *

class RegForm(forms.ModelForm):

    class Meta:
        model = Reg
        fields = '__all__'


class FileForm(forms.ModelForm):

    class Meta:
        model = Files
        fields = ['upload']	