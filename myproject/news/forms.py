from django import forms
from .models import NewsPost

class NewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'short_description', 'text']