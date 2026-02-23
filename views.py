"""
Fleet Management Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('fleet', 'dashboard')
@htmx_view('fleet/pages/dashboard.html', 'fleet/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('fleet', 'vehicles')
@htmx_view('fleet/pages/vehicles.html', 'fleet/partials/vehicles_content.html')
def vehicles(request):
    """Vehicles view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('fleet', 'settings')
@htmx_view('fleet/pages/settings.html', 'fleet/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}

