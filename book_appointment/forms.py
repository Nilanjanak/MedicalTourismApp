from django import forms
from .models import Booking  # Make sure Booking is imported correctly

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'age', 'phone', 'sex', 'address', 'time_slot', 'emergency_contact']
