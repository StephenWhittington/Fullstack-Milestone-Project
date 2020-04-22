from django import forms
from .models import Comment


class CommentPostForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('title', 'content', 'image', 'tag', 'published_date')