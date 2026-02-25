from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

VEH_STATUS = [
    ('available', _('Available')),
    ('in_use', _('In Use')),
    ('maintenance', _('In Maintenance')),
    ('retired', _('Retired')),
]

class Vehicle(HubBaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    plate_number = models.CharField(max_length=20, verbose_name=_('Plate Number'))
    make = models.CharField(max_length=100, blank=True, verbose_name=_('Make'))
    model = models.CharField(max_length=100, blank=True, verbose_name=_('Model'))
    year = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Year'))
    odometer = models.PositiveIntegerField(default=0, verbose_name=_('Odometer'))
    fuel_type = models.CharField(max_length=20, default='gasoline', verbose_name=_('Fuel Type'))
    status = models.CharField(max_length=20, default='available', choices=VEH_STATUS, verbose_name=_('Status'))
    assigned_to = models.UUIDField(null=True, blank=True, verbose_name=_('Assigned To'))
    notes = models.TextField(blank=True, verbose_name=_('Notes'))

    class Meta(HubBaseModel.Meta):
        db_table = 'fleet_vehicle'

    def __str__(self):
        return self.name


class FuelLog(HubBaseModel):
    """Fuel consumption record for a vehicle."""
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, related_name='fuel_logs')
    date = models.DateField(verbose_name=_('Date'))
    liters = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('Liters'))
    cost = models.DecimalField(max_digits=10, decimal_places=2, default='0', verbose_name=_('Cost'))
    odometer = models.PositiveIntegerField(verbose_name=_('Odometer Reading'))
    full_tank = models.BooleanField(default=True, verbose_name=_('Full Tank'))
    station = models.CharField(max_length=255, blank=True, verbose_name=_('Station'))
    notes = models.TextField(blank=True, verbose_name=_('Notes'))

    class Meta(HubBaseModel.Meta):
        db_table = 'fleet_fuellog'
        ordering = ['-date']

    def __str__(self):
        return f'{self.vehicle.name} - {self.date} - {self.liters}L'


class TripLog(HubBaseModel):
    """Trip record for a vehicle."""
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, related_name='trip_logs')
    date = models.DateField(verbose_name=_('Date'))
    origin = models.CharField(max_length=255, verbose_name=_('Origin'))
    destination = models.CharField(max_length=255, verbose_name=_('Destination'))
    distance_km = models.DecimalField(max_digits=8, decimal_places=1, default='0', verbose_name=_('Distance (km)'))
    driver_name = models.CharField(max_length=255, blank=True, verbose_name=_('Driver'))
    purpose = models.CharField(max_length=255, blank=True, verbose_name=_('Purpose'))
    notes = models.TextField(blank=True, verbose_name=_('Notes'))

    class Meta(HubBaseModel.Meta):
        db_table = 'fleet_triplog'
        ordering = ['-date']

    def __str__(self):
        return f'{self.vehicle.name} - {self.origin} → {self.destination}'


class VehicleMaintenanceLog(HubBaseModel):
    """Maintenance record for a vehicle."""
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, related_name='maintenance_logs')
    maintenance_type = models.CharField(
        max_length=20, default='corrective',
        choices=[
            ('preventive', _('Preventive')),
            ('corrective', _('Corrective')),
            ('inspection', _('Inspection / ITV')),
        ],
        verbose_name=_('Type'),
    )
    date = models.DateField(verbose_name=_('Date'))
    description = models.TextField(verbose_name=_('Description'))
    cost = models.DecimalField(max_digits=10, decimal_places=2, default='0', verbose_name=_('Cost'))
    odometer = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Odometer Reading'))
    performed_by = models.CharField(max_length=255, blank=True, verbose_name=_('Workshop / Mechanic'))
    next_maintenance = models.DateField(null=True, blank=True, verbose_name=_('Next Maintenance'))
    next_odometer = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Next at Odometer'))
    notes = models.TextField(blank=True, verbose_name=_('Notes'))

    class Meta(HubBaseModel.Meta):
        db_table = 'fleet_maintenancelog'
        ordering = ['-date']

    def __str__(self):
        return f'{self.vehicle.name} - {self.maintenance_type} - {self.date}'
