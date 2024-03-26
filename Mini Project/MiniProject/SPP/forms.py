# forms.py

from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)