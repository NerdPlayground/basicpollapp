from django import forms
from choices.models import Choice

class ChoicesForm(forms.ModelForm):
    class Meta:
        model= Choice
        fields= ["body"]