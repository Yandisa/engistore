from django.db import models
from inventory.models import Part


class Supplier(models.Model):
    """
    Represents a supplier that provides parts.

    Fields:
    - name: Supplier's company name
    - contact_email: Supplier's email address
    - phone: Contact number for quick communication
    - parts_supplied: Parts this supplier can provide
    """
    name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20)
    parts_supplied = models.ManyToManyField(Part, blank=True)

    def __str__(self):
        return self.name
