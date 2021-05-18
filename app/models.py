from django.db import models

# Create your models here.
from .system.models import CustomerProfile

from .features.quotation.models import Quotation
from .features.vehicle.models import Vehicle
from .features.coverage_setting.models import CoverageSetting