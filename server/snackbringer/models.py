from django.db import models
from carrier.models import Carrier

class SnackBringer(model.Models):
    name = models.CharField()
    last_updated = models.DateTimeField(auto_now=True)
    phone_number = models.BigIntegerField()
    carrier = models.ForeignKey(Carrier, on_delete=models.PREVENT)
    spouse = models.OneToOneField(SnackBringer, on_delete=models.PREVENT, null=True)
    active = models.BooleanField(default=True)
    has_car = models.BooleanField()

    def __str__(self):
        return name

    class Meta:
        ordering = ['-id']
        db_table = "snack_bringer"