from django import forms

from .models import form

class PostForm(forms.ModelForm):

    class Meta:
        model = form
        fields = ('name', 'emailid', 'reviews')
