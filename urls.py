from django.urls import path
from . import views

app_name = 'fleet'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('settings/', views.settings, name='settings'),
]
