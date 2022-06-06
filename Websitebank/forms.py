from tkinter.tix import Tree
from django import forms
from .models import profiles, payments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class profileregisterform(forms.ModelForm):
    class Meta:
        model = profiles
        fields = ['first_name','last_name','pin','card_no','balance']


class transactionforms(forms.ModelForm):
    class Meta:
        model = payments
        fields = ['receiver_no','amount','notes']

# class picupdateform(forms.ModelForm):
#     class Meta : 
#         model = profilepic
#         fields = ['image']
 
# class userupdateform(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username']

# class nodefluxphotoform(forms.ModelForm):
#     class Meta:
#         model = photos
#         fields = ['image']