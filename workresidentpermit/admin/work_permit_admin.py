from django.contrib import admin
from typing import Tuple

from base_module.admin_mixins import (
    BaseUrlModelAdminMixin, ModelAdminAuditFieldsMixin, audit_fieldset_tuple)

from ..admin_site import workresidencepermit_admin
from ..forms.work_only_permit_form import WorkPermitForm
from ..models import WorkPermit


@admin.register(WorkPermit, site=workresidencepermit_admin)
class WorkPermitAdmin(ModelAdminAuditFieldsMixin, BaseUrlModelAdminMixin, admin.ModelAdmin):

    form = WorkPermitForm
    list_display: Tuple[str, ...] = ('document_number', 'permit_status', 'job_offer', 'qualification', 'years_of_study')
    search_fields: Tuple[str, ...] = ('document_number',)

    fieldsets = (
        ("Occupation and Education", {
            "fields": (

            ),
        }),
        ("Work Details", {
            "fields": (
                "job_title",
                "job_description",
                "type_of_service",
                "address",
                "renumeration",
                "period_permit_sought",
                "has_vacancy_advertised",
                "labour_enquires",
            ),
        }),
        ("Training Localization Programme", {
            "fields": (

            ),
        }),
        audit_fieldset_tuple
    )

    # radio_fields = {"has_vacancy_advertised": admin.VERTICAL, }

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('document_number',)
        return self.readonly_fields
