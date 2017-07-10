from django import forms

from .models import Postimade

class PostForm(forms.ModelForm):

    class Meta:
        model = Postimade
        fields = ('title', 'text',)