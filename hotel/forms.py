from django import forms

from .models import Booking

class BokingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('full_name', 'email',
                    'check_in_date', 'check_out_date',
                    'num_adults', 'num_children' )
        