import os
import glob

from datetime import date

from faker import Faker

from app.api.dto import ApplicationVerificationRequestDTO, RecommendationRequestDTO, SecurityClearanceRequestDTO, \
    PresRecommendationRequestDTO
from app.api.serializers import (
    ApplicationVerificationRequestSerializer,
    RecommendationRequestDTOSerializer, SecurityClearanceRequestDTOSerializer, PresRecommendationDecisionSerializer,
)
from app.models import ApplicationStatus, ApplicationDecisionType, PresRecommendationDecision
from app.classes import ApplicationService

from app.api import NewApplicationDTO
from app.service import VerificationService, SecurityClearanceService
from app.service.pres_recommendation_decision import PresRecommendationDecisionService
from app.service.recommendation_service import RecommendationServiceOverideVetting
from app.validators import OfficerVerificationValidator, SecurityClearanceValidator
from app_assessment.api.dto import AssessmentCaseDecisionDTO
from app_assessment.service.assessment_note_service import AssessmentNoteService
from app_assessment.validators.assessment_note_validator import (
    AssessmentNoteValidator,
)
from app_assessment.api.dto.dto_serializers import AssessmentNoteRequestDTOSerializer
from app_assessment.api.dto.assessment_note_request_dto import (
    AssessmentNoteRequestDTO,
)
from app_assessment.service.assessment_case_decision_service import (
    AssessmentCaseDecisionService,
)
from app_assessment.validators.assessment_case_decision_validator import (
    AssessmentCaseDecisionValidator,
)
from app_assessment.api.serializers.assessement_request_serializer import (
    AssessmentRequestSerializer,
)

from app_personal_details.models import Person, Passport
from app_address.models import ApplicationAddress, Country
from app_contact.models import ApplicationContact

from django.apps import apps
from app_checklist.apps import AppChecklistConfig

from app_checklist.models import ClassifierItem
from app_attachments.models import ApplicationAttachment, AttachmentDocumentType
from app.utils import ApplicationStatusEnum, ApplicationDecisionEnum

from app.utils import statuses
from django.test import TestCase

from citizenship.api.dto import RecommendationDecisionRequestDTO
from citizenship.api.dto.citizenship_minister_decision_request_dto import \
    CitizenshipMinisterDecisionRequestDTOSerializer
from citizenship.api.dto.request_dto import CitizenshipMinisterRequestDTO
from citizenship.service.recommendation import RecommendationDecisionService, CitizenshipPresidentDecisionService
from citizenship.service.recommendation.citizenship_minister_decision_service import CitizenshipMinisterDecisionService
from citizenship.utils import CitizenshipProcessEnum


class BaseSetup(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        app_config = apps.get_app_config("app_checklist")
        if isinstance(app_config, AppChecklistConfig):
            app_config.ready()

    def application_decision_type(self):
        for value in [
            ApplicationDecisionEnum.ACCEPTED.value,
            ApplicationDecisionEnum.APPROVED.value,
            ApplicationDecisionEnum.PENDING.value,
            ApplicationDecisionEnum.REJECTED.value,
        ]:
            ApplicationDecisionType.objects.create(
                code=value,
                name=value,
                process_types=CitizenshipProcessEnum.RENUNCIATION.value,
                valid_from=date(2024, 1, 1),
                valid_to=date(2025, 1, 1),
            )

    def create_new_application(self):
        self.new_application_dto = NewApplicationDTO(
            process_name=CitizenshipProcessEnum.RENUNCIATION.value,
            applicant_identifier="317918515",
            status=ApplicationStatusEnum.VERIFICATION.value,
            dob="06101990",
            work_place="01",
            application_type=CitizenshipProcessEnum.RENUNCIATION.value,
            full_name="Test test",
            applicant_type="applicant",
        )
        self.application_service = ApplicationService(
            new_application_dto=self.new_application_dto
        )
        return self.application_service.create_application()

    def create_application_statuses(self):
        for status in statuses:
            ApplicationStatus.objects.create(**status)

    def create_personal_details(self, application, faker):
        return Person.objects.get_or_create(
            document_number=application.application_document.document_number,
            application_version=None,
            first_name=faker.unique.first_name(),
            last_name=faker.unique.last_name(),
            dob=faker.date_of_birth(minimum_age=18, maximum_age=65),
            middle_name=faker.first_name(),
            marital_status=faker.random_element(
                elements=("single", "married", "divorced")
            ),
            # country_birth=faker.country(),
            # place_birth=faker.city(),
            gender=faker.random_element(elements=("male", "female")),
            occupation=faker.job(),
            qualification=faker.random_element(
                elements=("diploma", "degree", "masters", "phd")
            ),
        )

    def create_address(self, app, faker):
        country = Country.objects.create(name=faker.country())
        return ApplicationAddress.objects.create(
            application_version=None,
            document_number=app.application_document.document_number,
            po_box=faker.address(),
            apartment_number=faker.building_number(),
            plot_number=faker.building_number(),
            address_type=faker.random_element(
                elements=("residential", "postal", "business", "private", "other")
            ),
            country=country,
            status=faker.random_element(elements=("active", "inactive")),
            city=faker.city(),
            street_address=faker.street_name(),
            private_bag=faker.building_number(),
        )

    def perform_verification(self):
        data = {"status": "ACCEPTED"}
        serializer = ApplicationVerificationRequestSerializer(data=data)
        serializer.is_valid()
        validator = OfficerVerificationValidator(document_number=self.document_number)
        if validator.is_valid():
            verification_request = ApplicationVerificationRequestDTO(
                document_number=self.document_number,
                user=None,
                **serializer.validated_data,
            )
            service = VerificationService(verification_request=verification_request)
            return service.create_verification()

    def perform_assessment(self):
        data = {"status": "ACCEPTED"}
        serializer = AssessmentRequestSerializer(data=data)
        serializer.is_valid()
        assessment_case_decision = AssessmentCaseDecisionDTO(
            document_number=self.document_number, decision="ACCEPTED", status="ACCEPTED"
        )
        validator = AssessmentCaseDecisionValidator(
            assessment_case_decision=assessment_case_decision,
        )

        if validator.is_valid():
            service = AssessmentCaseDecisionService(
                assessment_case_decision_dto=assessment_case_decision
            )
            return service.create_assessment()

    def perform_review(self):
        data = {"status": "ACCEPTED"}
        serializer = AssessmentNoteRequestDTOSerializer(data=data)
        serializer.is_valid()
        note_request_dto = AssessmentNoteRequestDTO(
            document_number=self.document_number, decision="ACCEPTED", status="ACCEPTED"
        )
        validator = AssessmentNoteValidator(
            assessment_note_request_dto=note_request_dto
        )

        if validator.is_valid():
            service = AssessmentNoteService(note_request_dto=note_request_dto)
            return service.create_review()

    def perform_recommendation(self):
        data = {"status": "ACCEPTED"}
        serializer = RecommendationRequestDTOSerializer(data=data)
        serializer.is_valid()
        data = serializer.validated_data
        request_dto = RecommendationDecisionRequestDTO(
            document_number=self.document_number,
            user=None,
            status="ACCEPTED",
            **data,
        )
        service = RecommendationDecisionService(decision_request=request_dto)
        return service.create_recommendation()

    def perform_pres_recommendation(self, role):
        data = {"status": "ACCEPTED"}
        serializer = PresRecommendationDecisionSerializer(data=data)
        serializer.is_valid()
        request_dto = PresRecommendationRequestDTO(
            document_number=self.document_number,
            user=None,
            status="ACCEPTED",
            role=role,
        )
        service = PresRecommendationDecisionService(decision_request=request_dto)
        return service.create_decision(PresRecommendationDecision, PresRecommendationDecisionSerializer)

    def perform_minister_decision(self):
        data = {"status": "ACCEPTED",
                'document_number': self.document_number}
        serializer = CitizenshipMinisterDecisionRequestDTOSerializer(data=data)
        serializer.is_valid()
        request = CitizenshipMinisterRequestDTO(document_number=self.document_number,
                                                    status="ACCEPTED",
                                                    **serializer.validated_data)
        service = CitizenshipMinisterDecisionService(decision_request=request)
        return service.create_minister_decision()

    def perform_president_decision(self):
        data = {"status": "ACCEPTED"}
        serializer = CitizenshipMinisterDecisionRequestDTOSerializer(data=data)
        serializer.is_valid()
        request = CitizenshipMinisterRequestDTO(document_number=self.document_number,
                                                    status="ACCEPTED",
                                                    **serializer.validated_data)
        service = CitizenshipPresidentDecisionService(decision_request=request)
        return service.create_president_decision()

    def perform_minister_decision_reject(self):
        data = {"status": "REJECTED"}
        serializer = CitizenshipMinisterDecisionRequestDTOSerializer(data=data)
        serializer.is_valid()
        request = CitizenshipMinisterRequestDTO(document_number=self.document_number,
                                                    status="REJECTED",
                                                    **serializer.validated_data)
        service = CitizenshipMinisterDecisionService(decision_request=request)
        return service.create_minister_decision()

    def perform_vetting(self):
        data = {"status": "ACCEPTED"}
        serializer = SecurityClearanceRequestDTOSerializer(data=data)
        if serializer.is_valid():
            security_clearance_request = SecurityClearanceRequestDTO(
                document_number=self.document_number,
                user=None,
                **serializer.validated_data,
            )
            validator = SecurityClearanceValidator(
                document_number=self.document_number,
                status=security_clearance_request.status,
            )
            if validator.is_valid():
                service = SecurityClearanceService(
                    security_clearance_request=security_clearance_request
                )
                return service.create_clearance()

    def setUp(self) -> None:

        self.create_application_statuses()
        self.application_decision_type()
        application_version = self.create_new_application()

        app = application_version.application
        self.application = application_version.application
        self.document_number = app.application_document.document_number
        faker = Faker()
        self.create_personal_details(app, faker)
        self.create_address(app, faker)

        ApplicationContact.objects.create(
            application_version=None,
            document_number=app.application_document.document_number,
            contact_type=faker.random_element(
                elements=("cell", "email", "fax", "landline")
            ),
            contact_value=faker.phone_number(),
            preferred_method_comm=faker.boolean(chance_of_getting_true=50),
            status=faker.random_element(elements=("active", "inactive")),
            description=faker.text(),
        )

        Passport.objects.create(
            application_version=None,
            document_number=app.application_document.document_number,
            passport_number=faker.passport_number(),
            date_issued=faker.date_this_century(),
            expiry_date=faker.date_this_century(),
            place_issued=faker.city(),
            nationality=faker.country(),
            photo=faker.image_url(),
        )
        # Checklist for process
        classifer_attachment_types = ClassifierItem.objects.filter(
            code__iexact="CITIZENSHIP_ATTACHMENT_DOCUMENTS"
        )

        for classifier in classifer_attachment_types:
            attachment_type = AttachmentDocumentType.objects.create(
                code=classifier.code,
                name=classifier.name,
                valid_from=date.today(),
                valid_to=date(2025, 1, 1),
            )
            ApplicationAttachment.objects.create(
                document_number=app.application_document.document_number,
                document_type=attachment_type,
                filename=f"{classifier.name}.pdf",
                storage_object_key="cxxcc",
                description="NNNN",
                document_url="",
                received_date=date.today(),
            )
