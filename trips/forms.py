from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['aircraft', 'origin', 'destination', 'departure_date_time', 'arrival_date_time', 'flight_time']
        widgets = {
            'departure_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


