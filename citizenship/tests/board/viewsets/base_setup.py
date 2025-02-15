from datetime import date
from django.utils import timezone

from django.urls import reverse

from faker import Faker

from app.models import ApplicationStatus
from app.classes import ApplicationService

from app.api import NewApplicationDTO

from app_personal_details.models import Person, Passport
from app_address.models import ApplicationAddress, Country
from app_contact.models import ApplicationContact

from django.apps import apps
from app_checklist.apps import AppChecklistConfig

from app_checklist.models import ClassifierItem, Region
from app_attachments.models import ApplicationAttachment, AttachmentDocumentType
from app.utils import ApplicationStatusEnum

from app.utils import statuses
from authentication.models import User
from citizenship.models import Role, BoardMember, Meeting, MeetingSession, Batch, Board

from citizenship.utils import CitizenshipProcessEnum

from rest_framework.test import APITestCase


class BaseSetup(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        app_config = apps.get_app_config('app_checklist')
        if isinstance(app_config, AppChecklistConfig):
            app_config.ready()

    def create_new_application(self, applicant_type=None):
        self.new_application_dto = NewApplicationDTO(
            process_name=CitizenshipProcessEnum.RENUNCIATION.value,
            applicant_identifier='317918515',
            status=ApplicationStatusEnum.NEW.value,
            dob="06101990",
            work_place="01",
            application_type=CitizenshipProcessEnum.RENUNCIATION.value,
            full_name="Test test",
            applicant_type="student" or applicant_type
        )

        self.application_service = ApplicationService(
            new_application_dto=self.new_application_dto)
        return self.application_service.create_application()

    def create_application_statuses(self):
        for status in statuses:
            ApplicationStatus.objects.create(
                **status
            )

    def create_personal_details(self, application, faker):
        return Person.objects.get_or_create(
            document_number=application.application_document.document_number,
            application_version=None,
            first_name=faker.unique.first_name(),
            last_name=faker.unique.last_name(),
            dob=faker.date_of_birth(minimum_age=18, maximum_age=65),
            middle_name=faker.first_name(),
            marital_status=faker.random_element(elements=('single', 'married', 'divorced')),
            # country_birth=faker.country(),
            # place_birth=faker.city(),
            gender=faker.random_element(elements=('male', 'female')),
            occupation=faker.job(),
            qualification=faker.random_element(elements=('diploma', 'degree', 'masters', 'phd'))
        )

    def create_address(self, app, faker):
        country = Country.objects.create(name=faker.country())
        return ApplicationAddress.objects.create(
            application_version=None,
            document_number=app.application_document.document_number,
            po_box=faker.address(),
            apartment_number=faker.building_number(),
            plot_number=faker.building_number(),
            address_type=faker.random_element(elements=('residential', 'postal', 'business', 'private',
                                                        'other')),
            country=country,
            city=faker.city(),
            street_address=faker.street_name(),
            private_bag=faker.building_number(),
        )
    def create_region(self):
        return Region.objects.create(
            name='Test Region',
            code='TR01',
            description='A test region',
            valid_from=timezone.now().date(),
            valid_to=(timezone.now() + timezone.timedelta(days=365)).date(),
            active=True
        )

    def create_board(self, region):
        role1 = Role.objects.create(name='Role 1', description='First role')
        role2 = Role.objects.create(name='Role 2', description='Second role')
        board = Board.objects.create(
            name='Test Board',
            region=region,
            description='A test board'
        )
        board.quorum_roles.set([role1, role2])
        board.save()
        return board

    def create_user_and_member(self, board, username="testuser", role="", description=""):
        user = User.objects.create_user(username=username, password='testpass')
        role = Role.objects.create(name=role, description=description)
        member = BoardMember.objects.create(user=user, board=board, role=role)
        return user, member

    def create_meeting(self, board):
        url = reverse('citizenship:meeting-list')
        self.client.post(url, {
            'title': 'New Meeting',
            'board': board.id,
            'location': 'New Location',
            'agenda': 'New Agenda',
            'start_date': "2024-08-01T14:30:00+0000",
            'end_date': "2024-08-01T14:30:00+0000",
            'time': '11:00:00'
        })
        return Meeting.objects.first()

    def create_meeting_session(self, meeting):
        url = reverse('citizenship:meeting-create-session', args=[meeting.id])
        data = {
            'title': 'Morning Session',
            'date': timezone.now().date().isoformat(),
            'start_time': '11:00:00',
            'end_time': '12:00:00'
        }
        self.client.post(url, data, format='json')
        return MeetingSession.objects.get(meeting=meeting)

    def create_batch(self, meeting):
        url = reverse('citizenship:batch-list')
        data = {
            'meeting': meeting.id,
            'name': 'New Test Batch'
        }
        self.client.post(url, data, format='json')
        return Batch.objects.first()

    def setUp(self) -> None:

        self.create_application_statuses()
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
            contact_type=faker.random_element(elements=('cell', 'email', 'fax', 'landline')),
            contact_value=faker.phone_number(),
            preferred_method_comm=faker.boolean(chance_of_getting_true=50),
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
            code__in=['PASSPORT_COPY', 'PASSPORT_PHOTO', 'COVER_LETTER']
        )

        for classifier in classifer_attachment_types:
            attachment_type = AttachmentDocumentType.objects.create(
                code=classifier.code,
                name=classifier.name,
                valid_from=date.today(),
                valid_to=date(2025, 1, 1)
            )
            ApplicationAttachment.objects.create(
                document_number=app.application_document.document_number,
                document_type=attachment_type,
                filename=f"{classifier.name}.pdf",
                storage_object_key="cxxcc",
                description="NNNN",
                document_url="",
                received_date=date.today()
            )
