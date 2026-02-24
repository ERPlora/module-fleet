"""Tests for fleet models."""
import pytest
from django.utils import timezone

from fleet.models import Vehicle


@pytest.mark.django_db
class TestVehicle:
    """Vehicle model tests."""

    def test_create(self, vehicle):
        """Test Vehicle creation."""
        assert vehicle.pk is not None
        assert vehicle.is_deleted is False

    def test_str(self, vehicle):
        """Test string representation."""
        assert str(vehicle) is not None
        assert len(str(vehicle)) > 0

    def test_soft_delete(self, vehicle):
        """Test soft delete."""
        pk = vehicle.pk
        vehicle.is_deleted = True
        vehicle.deleted_at = timezone.now()
        vehicle.save()
        assert not Vehicle.objects.filter(pk=pk).exists()
        assert Vehicle.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, vehicle):
        """Test default queryset excludes deleted."""
        vehicle.is_deleted = True
        vehicle.deleted_at = timezone.now()
        vehicle.save()
        assert Vehicle.objects.filter(hub_id=hub_id).count() == 0


