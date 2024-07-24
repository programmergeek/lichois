from django.db import transaction

from ..api.dto import SecurityClearanceRequestDTO
from ..api.serializers import SecurityClearanceSerializer
from ..models import SecurityClearance
from ..service import BaseDecisionService
from ..utils.system_enums import ApplicationStatusEnum
from ..workflow.transaction_data import VettingTransactionData


class SecurityClearanceService(BaseDecisionService):
    def __init__(
        self,
        security_clearance_request: SecurityClearanceRequestDTO,
        user=None,
    ):
        workflow = VettingTransactionData()
        workflow.vetting_decision = security_clearance_request.status
        workflow.vetting_obj_exists = True

        super().__init__(
            user,
            application_field_key="security_clearance",
            request=security_clearance_request,
            task_to_deactivate=ApplicationStatusEnum.VETTING.value,
            workflow=workflow,
        )
        self.application = super().get_application()

    @transaction.atomic
    def create_clearance(self):
        return self.create_decision(SecurityClearance, SecurityClearanceSerializer)
