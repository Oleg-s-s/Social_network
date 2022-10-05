from dataclasses import field
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
                attrs={
                    "placeholder": "Write something...",
                    "class": "textarea is-info is-medium",
                }
            ),
            label="",)

    class Meta:
        model = Post
        exclude = ("user", "likes")

class CommentForm(forms.ModelForm):
    text = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
                attrs={
                    "placeholder": "Write something...",
                    "class": "textarea is-info is-medium",
                }
            ),
            label="",)

    class Meta:
        model = Comment
        fields = ('text', )