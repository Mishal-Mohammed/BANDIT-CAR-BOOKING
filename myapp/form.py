from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control fw-bold '}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password', 'class' : 'form-control fw-bold'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password', 'class' : 'form-control fw-bold'}))