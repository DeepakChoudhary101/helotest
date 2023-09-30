from .models import userdata
from django import forms
class userdataform(forms.ModelForm):
    class Meta:
        model=userdata
        fields=['username','password']
