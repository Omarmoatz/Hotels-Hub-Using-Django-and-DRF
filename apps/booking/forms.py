from django import forms

from apps.booking.models import Booking


class BokingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            "full_name",
            "email",
            "check_in_date",
            "check_out_date",
            "num_adults",
            "num_children",
        )
        # widgets = {
        #     'user': forms.Select(attrs={'class': 'form-control'}),
        #     'event': forms.Select(attrs={'class': 'form-control'}),
        #     'sequence': forms.Select(attrs={'class': 'form-control'}),
        #     'price_per_ticket': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'tickets_count': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'order_status': forms.Select(attrs={'class': 'form-control'}),
        #     # 'invoice_id': forms.TextInput(attrs={'class': 'form-control'}),
        #     'payment_url': forms.URLInput(attrs={'class': 'form-control'}),
        # }
