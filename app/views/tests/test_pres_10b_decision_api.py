"""
Test President Decision for 10B api
"""
from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from app.api import NewApplicationDTO
from app.utils import ApplicationStatusEnum

from app.classes import ApplicationService
from app.api.serializers.pres_recommendation_decision_serializer import PresRecommendationDecisionSerializer

from app.models import Application
from citizenship.utils.citizenship_process_enum import CitizenshipProcessEnum
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from app.models import PresRecommendationDecision

PRES_DECISION_URL = reverse('pres-recommendation-decision-create')

def create_pres_decision(document_number, **params):

    defaults= {
        'date_approved': datetime.now(),
        'status': 'ACCEPTED',
        'approved_by': 'TEST',
        'role':'TEST'
    }

    defaults.update(**params)

    decision = PresRecommendationDecision.objects.create(document_number=document_number, **defaults)
    return decision

def details_url(document_id):
    """Returns the details url"""
    return reverse('pres-recommendation-decision-detail', args=[document_id])


class PublicPresDecision10BTests(TestCase):
    """Tests fot unauthenticated users"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Tests for authentication required."""
        res = self.client.get(PRES_DECISION_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivatePresDecision10BTests(TestCase):
    """Tests for authenticated users"""
    def setUp(self) -> None:

        self.client = APIClient()

        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword')

        self.client.force_authenticate(self.user)

        self.new_application_dto = NewApplicationDTO(
                process_name=CitizenshipProcessEnum.PRESIDENT_POWER_10B.value,
                applicant_identifier='317918515',
                status=ApplicationStatusEnum.VERIFICATION.value,
                dob="06101990",
                work_place="01",
                application_type=CitizenshipProcessEnum.PRESIDENT_POWER_10B.value,
                full_name="Test test",
                applicant_type="student"
            )

        self.application_service = ApplicationService(
                new_application_dto=self.new_application_dto)
        self.application_service.create_application()


    def test_retrieve_decision(self):
        """Test retrieve Pres Recommendation Decision"""

        app = Application.objects.get(
            application_document__document_number=self.document_number)
        create_pres_decision(role="PRESIDENT", document_number=app.application_document.document_number)
        res = self.client.get(PRES_DECISION_URL)

        decisions = PresRecommendationDecision.objects.all().order_by('-id')
        serializer = PresRecommendationDecisionSerializer(decisions, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
