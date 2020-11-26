from django import forms

from .models import *

class RegForm(forms.ModelForm):

    class Meta:
        model = Reg
        fields = '__all__'


class FilesForm(forms.ModelForm):

    class Meta:
        model = Fill
        fields = '__all__'


class JsonForm(forms.ModelForm):

    class Meta:
        model = Json
        fields = '__all__'
