from django.db import models

from base_module.model_mixins import BaseUuidModel
from identifier.non_citizen_identifier_model_mixins import (
    UniqueNonCitizenIdentifierFieldMixin,
)

recommendation_choices = (("yes", "Yes"), ("no", "No"))


class AssessmentRecommendation(UniqueNonCitizenIdentifierFieldMixin, BaseUuidModel):

    recommendation = models.CharField(
        verbose_name="Recommendation for PI status",
        max_length=12,
        choices=recommendation_choices,
        default="INCARCERATED",
    )

    asessment = models.TextField(verbose_name="Assessment")
