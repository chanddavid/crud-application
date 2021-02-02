# from django import forms
#
#
# class FormName(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     email = forms.CharField(max_length=100)

from django import forms
from django.forms import ModelForm

from .models import ModelName, Profile


class FormName(ModelForm):
    address = forms.CharField(max_length=100)

    class Meta:
        model = ModelName
        fields = ['first_name', 'last_name', 'email']


#
# class FormName2(ModelForm):
#     class Meta:
#         model=ModelName2
#         fields=['username','password']

# or bootstrap form use garda ni bho
class Loginform(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


#     widget le password *from ma dekhaunxa
class Loginform2(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)


class ProfileModel(forms.ModelForm):
    class Meta:
        models = Profile
        fields = ['image']
