from django import forms

from .models import formy

class PostForm(forms.ModelForm):

    class Meta:
        model = formy
        fields = ('name', 'emailid', 'reviews')
