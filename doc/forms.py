from django import forms

from .models import *

class RegForm(forms.ModelForm):

    class Meta:
        model = Reg
        fields = '__all__'
    # class Meta:
    #     model = Person
    #     model = Group
    #     model = Membership
    #     fields = '__all__'
