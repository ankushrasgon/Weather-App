from django import forms
from .models import City
from django.forms import TextInput

class CityForm(forms.ModelForm):
    class Meta:
        model=City
        fields=['city_name']
        widgets = {'city_name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Enter City Name'})}
