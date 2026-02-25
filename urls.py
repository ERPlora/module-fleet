from django.urls import path
from . import views

app_name = 'fleet'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Vehicle
    path('vehicles/', views.vehicles_list, name='vehicles_list'),
    path('vehicles/add/', views.vehicle_add, name='vehicle_add'),
    path('vehicles/<uuid:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('vehicles/<uuid:pk>/edit/', views.vehicle_edit, name='vehicle_edit'),
    path('vehicles/<uuid:pk>/delete/', views.vehicle_delete, name='vehicle_delete'),
    path('vehicles/bulk/', views.vehicles_bulk_action, name='vehicles_bulk_action'),

    # Fuel Logs
    path('vehicles/<uuid:pk>/fuel/add/', views.fuel_log_add, name='fuel_log_add'),
    path('vehicles/<uuid:pk>/fuel/<uuid:log_pk>/delete/', views.fuel_log_delete, name='fuel_log_delete'),

    # Trip Logs
    path('vehicles/<uuid:pk>/trips/add/', views.trip_log_add, name='trip_log_add'),
    path('vehicles/<uuid:pk>/trips/<uuid:log_pk>/delete/', views.trip_log_delete, name='trip_log_delete'),

    # Maintenance Logs
    path('vehicles/<uuid:pk>/maintenance/add/', views.maintenance_log_add, name='maintenance_log_add'),
    path('vehicles/<uuid:pk>/maintenance/<uuid:log_pk>/delete/', views.maintenance_log_delete, name='maintenance_log_delete'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]
