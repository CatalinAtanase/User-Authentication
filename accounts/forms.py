from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
from .models import Profile
from django.db import models

class UserRegistration(UserCreationForm):
    email = forms.EmailField()

    User._meta.get_field('email')._unique = True

    def clean_username(self):
        username_passed = self.cleaned_data.get('username')
        if len(User.objects.filter(username=username_passed)) > 0:
            raise forms.ValidationError('Exista deja un user cu acest nume de utilizator')
        return username_passed

    def clean_email(self):
        email_passed = self.cleaned_data.get('email')
        if len(User.objects.filter(email=email_passed)) > 0:
            raise forms.ValidationError('Exista deja un user cu aceasta adresa de email')
        
        return email_passed

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError('Parola trebuie sa fie de cel putin 8 caractere')
        
        return password1

    # def clean_password2(self):
    #     # Overwrite the method so u don't get 'Password is too short on both'
    #     # errors = []
    #     # raise forms.ValidationError(errors)
    #     # return self.cleaned_data.get('password2')
        

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image',
        ]
    