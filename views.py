"""
Fleet Management Module Views
"""
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, render as django_render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.core.services import export_to_csv, export_to_excel
from apps.modules_runtime.navigation import with_module_nav

from .models import Vehicle

PER_PAGE_CHOICES = [10, 25, 50, 100]


# ======================================================================
# Dashboard
# ======================================================================

@login_required
@with_module_nav('fleet', 'dashboard')
@htmx_view('fleet/pages/index.html', 'fleet/partials/dashboard_content.html')
def dashboard(request):
    hub_id = request.session.get('hub_id')
    return {
        'total_vehicles': Vehicle.objects.filter(hub_id=hub_id, is_deleted=False).count(),
    }


# ======================================================================
# Vehicle
# ======================================================================

VEHICLE_SORT_FIELDS = {
    'name': 'name',
    'status': 'status',
    'odometer': 'odometer',
    'year': 'year',
    'plate_number': 'plate_number',
    'make': 'make',
    'created_at': 'created_at',
}

def _build_vehicles_context(hub_id, per_page=10):
    qs = Vehicle.objects.filter(hub_id=hub_id, is_deleted=False).order_by('name')
    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(1)
    return {
        'vehicles': page_obj,
        'page_obj': page_obj,
        'search_query': '',
        'sort_field': 'name',
        'sort_dir': 'asc',
        'current_view': 'table',
        'per_page': per_page,
    }

def _render_vehicles_list(request, hub_id, per_page=10):
    ctx = _build_vehicles_context(hub_id, per_page)
    return django_render(request, 'fleet/partials/vehicles_list.html', ctx)

@login_required
@with_module_nav('fleet', 'vehicles')
@htmx_view('fleet/pages/vehicles.html', 'fleet/partials/vehicles_content.html')
def vehicles_list(request):
    hub_id = request.session.get('hub_id')
    search_query = request.GET.get('q', '').strip()
    sort_field = request.GET.get('sort', 'name')
    sort_dir = request.GET.get('dir', 'asc')
    page_number = request.GET.get('page', 1)
    current_view = request.GET.get('view', 'table')
    per_page = int(request.GET.get('per_page', 10))
    if per_page not in PER_PAGE_CHOICES:
        per_page = 10

    qs = Vehicle.objects.filter(hub_id=hub_id, is_deleted=False)

    if search_query:
        qs = qs.filter(Q(name__icontains=search_query) | Q(plate_number__icontains=search_query) | Q(make__icontains=search_query) | Q(model__icontains=search_query))

    order_by = VEHICLE_SORT_FIELDS.get(sort_field, 'name')
    if sort_dir == 'desc':
        order_by = f'-{order_by}'
    qs = qs.order_by(order_by)

    export_format = request.GET.get('export')
    if export_format in ('csv', 'excel'):
        fields = ['name', 'status', 'odometer', 'year', 'plate_number', 'make']
        headers = ['Name', 'Status', 'Odometer', 'Year', 'Plate Number', 'Make']
        if export_format == 'csv':
            return export_to_csv(qs, fields=fields, headers=headers, filename='vehicles.csv')
        return export_to_excel(qs, fields=fields, headers=headers, filename='vehicles.xlsx')

    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(page_number)

    if request.htmx and request.htmx.target == 'datatable-body':
        return django_render(request, 'fleet/partials/vehicles_list.html', {
            'vehicles': page_obj, 'page_obj': page_obj,
            'search_query': search_query, 'sort_field': sort_field,
            'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
        })

    return {
        'vehicles': page_obj, 'page_obj': page_obj,
        'search_query': search_query, 'sort_field': sort_field,
        'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
    }

@login_required
def vehicle_add(request):
    hub_id = request.session.get('hub_id')
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        plate_number = request.POST.get('plate_number', '').strip()
        make = request.POST.get('make', '').strip()
        model = request.POST.get('model', '').strip()
        year = int(request.POST.get('year', 0) or 0)
        odometer = int(request.POST.get('odometer', 0) or 0)
        fuel_type = request.POST.get('fuel_type', '').strip()
        status = request.POST.get('status', '').strip()
        assigned_to = request.POST.get('assigned_to', '').strip()
        notes = request.POST.get('notes', '').strip()
        obj = Vehicle(hub_id=hub_id)
        obj.name = name
        obj.plate_number = plate_number
        obj.make = make
        obj.model = model
        obj.year = year
        obj.odometer = odometer
        obj.fuel_type = fuel_type
        obj.status = status
        obj.assigned_to = assigned_to
        obj.notes = notes
        obj.save()
        return _render_vehicles_list(request, hub_id)
    return django_render(request, 'fleet/partials/panel_vehicle_add.html', {})

@login_required
def vehicle_edit(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(Vehicle, pk=pk, hub_id=hub_id, is_deleted=False)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '').strip()
        obj.plate_number = request.POST.get('plate_number', '').strip()
        obj.make = request.POST.get('make', '').strip()
        obj.model = request.POST.get('model', '').strip()
        obj.year = int(request.POST.get('year', 0) or 0)
        obj.odometer = int(request.POST.get('odometer', 0) or 0)
        obj.fuel_type = request.POST.get('fuel_type', '').strip()
        obj.status = request.POST.get('status', '').strip()
        obj.assigned_to = request.POST.get('assigned_to', '').strip()
        obj.notes = request.POST.get('notes', '').strip()
        obj.save()
        return _render_vehicles_list(request, hub_id)
    return django_render(request, 'fleet/partials/panel_vehicle_edit.html', {'obj': obj})

@login_required
@require_POST
def vehicle_delete(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(Vehicle, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_deleted = True
    obj.deleted_at = timezone.now()
    obj.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])
    return _render_vehicles_list(request, hub_id)

@login_required
@require_POST
def vehicles_bulk_action(request):
    hub_id = request.session.get('hub_id')
    ids = [i.strip() for i in request.POST.get('ids', '').split(',') if i.strip()]
    action = request.POST.get('action', '')
    qs = Vehicle.objects.filter(hub_id=hub_id, is_deleted=False, id__in=ids)
    if action == 'delete':
        qs.update(is_deleted=True, deleted_at=timezone.now())
    return _render_vehicles_list(request, hub_id)


@login_required
@with_module_nav('fleet', 'settings')
@htmx_view('fleet/pages/settings.html', 'fleet/partials/settings_content.html')
def settings_view(request):
    return {}

