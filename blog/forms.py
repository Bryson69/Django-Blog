from django import forms

from django.contrib.auth.models import User
from django.forms import widgets

from .models import Comment

class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # derrick macharia
            # 
        }
