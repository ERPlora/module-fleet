from django.contrib import admin

from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['name', 'plate_number', 'make', 'model', 'year', 'created_at']
    search_fields = ['name', 'plate_number', 'make', 'model']
    readonly_fields = ['created_at', 'updated_at']

