from base_module.model_fields import UUIDAutoField
from django.db import models

from app.models import ApplicationBaseModel

from .assessment_update_mixin import AssessmentUpdateMixin
from .choices import DECISION_TYPE


class AssessmentCaseDecision(ApplicationBaseModel, AssessmentUpdateMixin):

    parent_object_id = UUIDAutoField(
        blank=True,
        editable=False,
        help_text="Parent ID primary key.",
    )

    parent_object_type = models.CharField(max_length=200, null=False, blank=True)

    author = models.CharField(max_length=200)

    author_role = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)

    decision = models.CharField(
        max_length=200, choices=DECISION_TYPE, null=False, blank=True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.save_assessment()

    class Meta:
        db_table = "assessment_case_decisions"
        verbose_name = "Assessment Case Decision"
        verbose_name_plural = "Assessment Case Decision"
