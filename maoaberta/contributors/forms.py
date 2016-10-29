from django.contrib.auth import views as auth_views
from django.forms.widgets import TextInput
from django import forms


class LoginForm(auth_views.forms.AuthenticationForm):
    username = forms.CharField(max_length=100)

    class Meta:
        widgets = {
            'username': TextInput(attrs={
                'required': 'required',
                'focus': 'focus',
                'class': 'form-control'
            })
        }
