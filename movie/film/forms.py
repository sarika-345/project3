from django import forms
from film.models import Film


class filmform(forms.ModelForm):   #form definition
    class Meta:
        model=Film
        fields='__all__'