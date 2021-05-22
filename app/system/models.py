from django.db import models
from django.contrib.auth.models import User

from app.features.quotation.models import Quotation

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=17, unique=True)

    quotation = models.ForeignKey(Quotation, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'quotation'], name='unique user-quotation')
        ]