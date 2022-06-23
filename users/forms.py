from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy


class UserRegistrationForm(UserCreationForm, forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()    
        self.helper.form_action = reverse_lazy('register')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholders': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={ 
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
         widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    