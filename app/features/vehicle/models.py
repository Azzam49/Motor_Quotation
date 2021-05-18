from django.db import models

class Vehicle(models.Model):
    model = models.CharField(max_length=80, verbose_name='Vehicle Model')
    number = models.CharField(max_length=40, verbose_name='Vehicle No.')
    year_make = models.CharField(max_length=40, verbose_name='Vehicle Year Make')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=100000.00, verbose_name='Vehicle Price')

    def __str__(self):
        return self.model