from django.urls import path
from . import views

app_name = 'fleet'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Vehicle
    path('vehicles/', views.vehicles_list, name='vehicles_list'),
    path('vehicles/add/', views.vehicle_add, name='vehicle_add'),
    path('vehicles/<uuid:pk>/edit/', views.vehicle_edit, name='vehicle_edit'),
    path('vehicles/<uuid:pk>/delete/', views.vehicle_delete, name='vehicle_delete'),
    path('vehicles/bulk/', views.vehicles_bulk_action, name='vehicles_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]
