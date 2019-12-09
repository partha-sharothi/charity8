from django.forms import ModelForm
from django import forms
from .models import UserProfileInfo,Support
from django.contrib.auth.models import User
# from member.models import UserA

# class RegistrationFromA(ModelForm):
#     class Meta:
#         model  = UserA
#         fields = ['first_name','last_name']

class UserProfileInfoForm(ModelForm):
    
    class Meta:
        model = UserProfileInfo
        fields = ('phone_number','sponsor','country')


class UserForm(ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')        

class UserFormUpdate(ModelForm):

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email') 


class BalanceTransferForm(forms.Form):
    username = forms.CharField(max_length = 150)
    amount = forms.IntegerField()

class AccoutActivationForm(forms.Form):
    username = forms.CharField(max_length = 150)
    amount = forms.IntegerField()

class WithdrawalFundForm(forms.Form):
    amount = forms.IntegerField() 
    


class BitcoinDetailForm(forms.Form):
    bitcoin_address = forms.CharField(max_length = 200)


class SupportForm(ModelForm):
    class Meta:
        model = Support
        fields = ('user','subject','details')