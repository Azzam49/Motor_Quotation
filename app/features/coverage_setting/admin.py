from django.contrib import admin
from .models import CoverageSetting

@admin.register(CoverageSetting)
class CoverageSettingAdmin(admin.ModelAdmin):

    def __str__(self):
        return f"{self.name} - {self.value}"
