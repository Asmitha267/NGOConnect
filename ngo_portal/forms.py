# ngo_portal/forms.py
from django import forms
from .models import NGOEvent, VolunteerApplication

class NGOEventForm(forms.ModelForm):
    class Meta:
        model = NGOEvent
        fields = ['title', 'description', 'location', 'date']

class VolunteerApplicationForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ['motivation']
