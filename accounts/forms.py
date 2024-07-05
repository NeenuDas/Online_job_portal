from typing import Any
from django.forms import ModelForm, Form, EmailInput, Select, RadioSelect, CheckboxInput
from django.forms import TextInput, PasswordInput, CharField, Textarea, FileInput, DateInput,NumberInput,IntegerField,ImageField,ClearableFileInput,ChoiceField,DateField,SelectMultiple
from .models import *
from django.core.validators import MinLengthValidator
from django import forms


class LoginForm(Form):
    username = CharField(
        max_length = 15,
        min_length = 4,
        required = True,
        widget = TextInput({
            'class': 'form-control',
            'placeholder':'Username'
        })
    )

    password = CharField(
        max_length = 15,
        min_length = 4,
        required = True,
        widget = PasswordInput({
            'class': 'form-control',
            'placeholder':'Password'
        })
    )


class UserRegisterForm(ModelForm):

    confirm_password = CharField(
        max_length=25,
        min_length=8,
        required=True,
        validators=[
            MinLengthValidator(8,'Password is too short!')
        ],
        widget= PasswordInput({
            'class':'form-control',
            'placeholder':'Confirm Password'
        })
    )

    
    class Meta():
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',

        ]
        
        widgets = {
            'first_name': TextInput({
                'class':'form-control',
                'placeholder':'Firstname'
            }),

            'last_name': TextInput({
                'class':'form-control',
                'placeholder':'Lastname'
            }),

            'username': TextInput({
                'class':'form-control',
                'placeholder':'Username'
            }),

            'email': EmailInput({
                'class':'form-control',
                'placeholder':'Email'
            }),

            'password': PasswordInput({
                'class':'form-control',
                'placeholder':'Password'
            }),

        }
class DetailRegistration(ModelForm):
    class Meta():
        model = User
        fields = [
            'phone',
            'profile_photo',
            'dob',
            'short_bio',
            'job_title',
            'gender',
            'country',
            'open_to_hiring'
        ]
        
        widgets = {

            'phone': TextInput({
                'class':'form-control',
                'placeholder':'Phone'
            }),

            'dob': DateInput({
                'class': 'form-control'
            }),

            'short_bio': Textarea({
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Short Bio'
            }),

            'job_title': TextInput({
                'class': 'form-control',
                'placeholder': 'Job Title'
            }),

            'gender': Select({
                'class': 'form-control'
            }),

            'country': Select({
                'class': 'form-control'
            }),

            'open_to_hiring': CheckboxInput(),

            'profile_photo': FileInput({
                'class': 'form-control'
            })
        }
    

