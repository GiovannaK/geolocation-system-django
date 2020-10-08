from django.forms import ModelForm, TextInput
from .models import Location

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ('destination',)
        widgets = {'destination': TextInput(attrs={'class': 'materialize-textarea input-text'})}