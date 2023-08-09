from django import forms
from server.models import *
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField
    # birth_of_date = forms.DateField

    class Meta:
        model = Person
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'science',
                  'profession', 'photo', 'phone',
                  'city', 'twitter', 'facebook',
                  'youtube', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'birth_of_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class PersonUpdateForm(forms.ModelForm):
    email = forms.EmailField
    # birth_of_date = forms.DateField

    class Meta:
        model = Person
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'science',
                  'profession', 'photo', 'phone',
                  'city', 'twitter', 'facebook',
                  'youtube']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'birth_of_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Project


class MaterialForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Material

