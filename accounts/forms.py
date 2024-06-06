from typing import Any
from django import forms
from .models import Account

class RegistationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class' : 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class' : 'form-control',
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name','phone', 'email', 'password']

    def __init__(self, *args ,**kwargs):
        super(RegistationForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Phone Number'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    

    def clean(self):
        cleaned_data = super(RegistationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'password does not matched!'
            )