from django.utils.translation import gettext_lazy as _

MODULE_ID = 'fleet'
MODULE_NAME = _('Fleet Management')
MODULE_VERSION = '1.0.0'
MODULE_ICON = 'car-sport-outline'
MODULE_DESCRIPTION = _('Vehicle fleet tracking, fuel and maintenance')
MODULE_AUTHOR = 'ERPlora'
MODULE_CATEGORY = 'operations'

MENU = {
    'label': _('Fleet Management'),
    'icon': 'car-sport-outline',
    'order': 58,
}

NAVIGATION = [
    {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Vehicles'), 'icon': 'car-sport-outline', 'id': 'vehicles'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
]

DEPENDENCIES = []

PERMISSIONS = [
    'fleet.view_vehicle',
'fleet.add_vehicle',
'fleet.change_vehicle',
'fleet.delete_vehicle',
'fleet.manage_settings',
]
