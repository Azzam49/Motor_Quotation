from django.contrib import admin

# Register your models here.
from .system.admin import CustomerProfileAdmin
from .system.admin import CustomUserAdmin

from .features.quotation.admin import QuotationAdmin
from .features.vehicle.admin import VehicleAdmin
from .features.coverage_setting.admin import CoverageSettingAdmin