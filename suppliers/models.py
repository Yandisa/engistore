from django.db import models
from inventory.models import Part


class Supplier(models.Model):
    """
    Represents a supplier entity.

    Fields:
        - name: Supplier name
        - contact_email: Email address of the supplier
        - phone: Contact phone number
        - parts_supplied: Parts this supplier provides (many-to-many relationship)
    """
    name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20)
    parts_supplied = models.ManyToManyField(Part, blank=True)

    def __str__(self):
        return self.name
