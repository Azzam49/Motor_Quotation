from django.db import models
from django.contrib.auth.models import User

from app.features.quotation.models import Quotation

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=17, unique=True)

    # TODO : many need to change to m2m relation, so a user can have more than one quotation,
    # also after login, on page view details of quotations also provide button to create more quotations
    quotation = models.ForeignKey(Quotation, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username