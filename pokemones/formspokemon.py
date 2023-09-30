from django import forms
from .models import POKEMON


class PokemonForm(forms.ModelForm):
    class Meta:
        model = POKEMON
        fields = '__all__'
