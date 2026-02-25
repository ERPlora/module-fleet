from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Vehicle, FuelLog, TripLog, VehicleMaintenanceLog

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

class FuelLogForm(forms.ModelForm):
    class Meta:
        model = FuelLog
        fields = ['vehicle', 'date', 'liters', 'cost', 'odometer', 'full_tank', 'station', 'notes']
        widgets = {
            'vehicle': forms.Select(attrs={'class': 'select select-sm w-full'}),
            'date': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
            'liters': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number', 'step': '0.01'}),
            'cost': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number', 'step': '0.01'}),
            'odometer': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'full_tank': forms.CheckboxInput(attrs={'class': 'toggle'}),
            'station': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'notes': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 2}),
        }

class TripLogForm(forms.ModelForm):
    class Meta:
        model = TripLog
        fields = ['vehicle', 'date', 'origin', 'destination', 'distance_km', 'driver_name', 'purpose', 'notes']
        widgets = {
            'vehicle': forms.Select(attrs={'class': 'select select-sm w-full'}),
            'date': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
            'origin': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'destination': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'distance_km': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number', 'step': '0.1'}),
            'driver_name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'purpose': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'notes': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 2}),
        }

class VehicleMaintenanceLogForm(forms.ModelForm):
    class Meta:
        model = VehicleMaintenanceLog
        fields = ['vehicle', 'maintenance_type', 'date', 'description', 'cost', 'odometer', 'performed_by', 'next_maintenance', 'next_odometer', 'notes']
        widgets = {
            'vehicle': forms.Select(attrs={'class': 'select select-sm w-full'}),
            'maintenance_type': forms.Select(attrs={'class': 'select select-sm w-full'}),
            'date': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 3}),
            'cost': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number', 'step': '0.01'}),
            'odometer': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'performed_by': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'next_maintenance': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
            'next_odometer': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'notes': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 2}),
        }
