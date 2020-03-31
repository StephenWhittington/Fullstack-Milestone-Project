from django import forms

class UserLoginForm(forms.Form):
    """form to log in users"""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)