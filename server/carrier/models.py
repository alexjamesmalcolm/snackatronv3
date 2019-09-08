from django.db import models

class Carrier(models.Model):
    name = models.CharField()
    sms_gateway = models.CharField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']
        db_table = "carrier"