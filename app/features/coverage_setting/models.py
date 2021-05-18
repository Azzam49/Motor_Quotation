from django.db import models

class CoverageSetting(models.Model):
    name = models.CharField(max_length=80, verbose_name='Coverage Name')
    value = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Coverage Value')

    def __str__(self):
        return f"{self.name} - {self.value}"