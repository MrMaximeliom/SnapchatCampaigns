from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email']
        def clean_username(self,username):
            from django.core.exceptions import ValidationError
            if User.objects.filter(username=username).exists():
                raise ValidationError('A user with this email already exists.')
            return  username


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

