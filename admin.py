from django.contrib import admin

from .models import Vehicle, FuelLog, TripLog, VehicleMaintenanceLog

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['name', 'plate_number', 'make', 'model', 'year', 'created_at']
    search_fields = ['name', 'plate_number', 'make', 'model']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(FuelLog)
class FuelLogAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'date', 'liters', 'cost', 'odometer', 'created_at']
    search_fields = ['station', 'notes']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(TripLog)
class TripLogAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'date', 'origin', 'destination', 'distance_km', 'created_at']
    search_fields = ['origin', 'destination', 'driver_name', 'purpose']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(VehicleMaintenanceLog)
class VehicleMaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'maintenance_type', 'date', 'cost', 'performed_by', 'created_at']
    search_fields = ['description', 'performed_by']
    readonly_fields = ['created_at', 'updated_at']
