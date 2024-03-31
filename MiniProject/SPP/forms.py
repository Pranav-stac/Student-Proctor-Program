# forms.py

from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

# forms.py
from django import forms
from .models import Certificate


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['certificate_name', 'image']

    # Add this method to ensure the file input field is rendered correctly
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'accept': 'image/*'})  # Allow only image files
