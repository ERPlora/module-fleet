from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'plate_number', 'make', 'model', 'year', 'odometer', 'fuel_type', 'status', 'assigned_to', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'plate_number': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'make': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'model': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'year': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'odometer': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'fuel_type': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'status': forms.Select(attrs={'class': 'select select-sm w-full'}),
            'assigned_to': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'notes': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 3}),
        }

