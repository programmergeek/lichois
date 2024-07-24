from re import A

from django.db import transaction

from ..api.dto import RecommendationRequestDTO
from ..api.serializers import CommissionerDecisionSerializer
from ..models import CommissionerDecision
from ..service import BaseDecisionService
from ..utils.system_enums import ApplicationStatusEnum
from ..workflow.transaction_data import RecommendationTransitionData


class RecommendationService(BaseDecisionService):
    def __init__(self, recommendation_request: RecommendationRequestDTO, user=None):

        workflow = RecommendationTransitionData()
        workflow.recommendation = recommendation_request.status

        super().__init__(
            request=recommendation_request,
            user=user,
            application_field_key="recommendation",
            workflow=workflow,
            task_to_deactivate=ApplicationStatusEnum.RECOMMENDATION.value,
        )

    @transaction.atomic
    def create_recommendation(self):
        return self.create_decision(
            CommissionerDecision, CommissionerDecisionSerializer
        )

    def retrieve_recommendation(self):
        return self.retrieve_decision(
            CommissionerDecision, CommissionerDecisionSerializer
        )
