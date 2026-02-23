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

