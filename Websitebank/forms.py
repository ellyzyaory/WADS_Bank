from tkinter.tix import Tree
from django import forms
from .models import  account_user, profile, transaction
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FormBank_Account(forms.ModelForm):
    class Meta:
        model= account_user
        fields= ['first_name', 'last_name', 'username','password','pin','card_no', 'balance']

class profileregisterform(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['first_name','last_name','pin','card_no','balance']


class transactionforms(forms.ModelForm):
    class Meta:
        model = transaction
        fields = ['receiver_no','amount','notes']

 
 