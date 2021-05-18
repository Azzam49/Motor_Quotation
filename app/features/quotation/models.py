from django.db import models
from django.utils import timezone

from app.features.vehicle.models import Vehicle

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

class Quotation(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    windscreen_coverage = models.BooleanField(default=False, choices=BOOL_CHOICES)
    passenger_liability_coverage = models.BooleanField(default=False, choices=BOOL_CHOICES)
    flood_coverage = models.BooleanField(default=False, choices=BOOL_CHOICES)
    windstorm_coverage = models.BooleanField(default=False, choices=BOOL_CHOICES)
    landslide_coverage = models.BooleanField(default=False, choices=BOOL_CHOICES)
    subsidence_coverage = models.BooleanField(default=False, choices=BOOL_CHOICES)
    create_date = models.DateTimeField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return self.name