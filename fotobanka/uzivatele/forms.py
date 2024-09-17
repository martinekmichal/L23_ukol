from django import forms
from .models import Data


class FotoForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['title', 'author', 'cena']
