from django import forms
from .models import Chat

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)