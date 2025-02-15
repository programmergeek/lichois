from django.db import models

from app.models import ApplicationBaseModel
from app_personal_details.choices import PERSON_TYPE
from .country import Country
from ..choices import ADDRESS_TYPE, ADDRESS_STATUS


class ApplicationAddress(ApplicationBaseModel):

    apartment_number = models.CharField(max_length=100, blank=True, null=True)
    plot_number = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True
    )

    city = models.CharField(max_length=100)

    district = models.JSONField(
        null=True, blank=True, db_column='district')

    village = models.JSONField(
        null=True, blank=True, db_column='village')

    ward = models.JSONField(
        null=True, blank=True, db_column='ward')

    street_address = models.CharField(max_length=255, blank=True, null=True)
    address_type = models.CharField(max_length=100, choices=ADDRESS_TYPE)
    status = models.CharField(max_length=100, choices=ADDRESS_STATUS, default="active")
    private_bag = models.CharField(max_length=100, blank=True, null=True)
    po_box = models.CharField(max_length=100, blank=True, null=True)

    person_type = models.CharField(
        max_length=150,
        choices=PERSON_TYPE,
        default="applicant",
    )

    def __str__(self):
        return f"{self.apartment_number}, {self.plot_number}, {self.street_address}, {self.city}, {self.country}"
