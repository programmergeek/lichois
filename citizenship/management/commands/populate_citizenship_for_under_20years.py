from django.db.transaction import atomic
from model_bakery import baker

from app_address.models import ApplicationAddress

from app_personal_details.models import Person
from lichois.management.base_command import CustomBaseCommand
from ...utils import CitizenshipProcessEnum
from ...models import FormE


class Command(CustomBaseCommand):
    help = "Populate data for Citizenship under 20 years service"
    process_name = CitizenshipProcessEnum.UNDER_20_CITIZENSHIP.value
    application_type = CitizenshipProcessEnum.UNDER_20_CITIZENSHIP.value

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(f"Process name {self.process_name}"))

        for _ in range(50):
            with atomic():
                # new_application
                app, version = self.create_basic_data()

                guardian = baker.make(
                    Person,
                    application_version=version,
                    document_number=app.application_document.document_number,
                    person_type="guardian",
                    first_name=self.faker.unique.first_name(),
                    last_name=self.faker.unique.last_name(),
                )

                guardian_address = baker.make(
                    ApplicationAddress,
                    application_version=version,
                    document_number=app.application_document.document_number,
                    po_box=self.faker.address(),
                    person_type="guardian",
                    city=self.faker.city(),
                )

                parent = baker.make(
                    Person,
                    application_version=version,
                    document_number=app.application_document.document_number,
                    person_type="father",
                    first_name=self.faker.unique.first_name(),
                    last_name=self.faker.unique.last_name(),
                )

                parent_address = baker.make(
                    ApplicationAddress,
                    application_version=version,
                    document_number=app.application_document.document_number,
                    po_box=self.faker.address(),
                    city=self.faker.city(),
                    person_type="father",
                )

                sponsor = baker.make(
                    Person,
                    application_version=version,
                    document_number=app.application_document.document_number,
                    person_type="sponsor",
                    first_name=self.faker.unique.first_name(),
                    last_name=self.faker.unique.last_name(),
                )

                sponsor_address = baker.make(
                    ApplicationAddress,
                    application_version=version,
                    document_number=app.application_document.document_number,
                    po_box=self.faker.address(),
                    person_type="sponsor",
                    city=self.faker.city(),
                )

                witness = baker.make(
                    Person,
                    application_version=version,
                    document_number=app.application_document.document_number,
                    person_type="witness",
                    first_name=self.faker.unique.first_name(),
                    last_name=self.faker.unique.last_name(),
                )

                waitness_address = baker.make(
                    ApplicationAddress,
                    application_version=version,
                    document_number=app.application_document.document_number,
                    po_box=self.faker.address(),
                    person_type="witness",
                    city=self.faker.city(),
                )

                baker.make(
                    FormE,
                    declaration_fname=self.faker.unique.first_name(),
                    declaration_lname=self.faker.unique.last_name(),
                    document_number=app.application_document.document_number,
                    guardian=guardian,
                    guardian_address=guardian_address,
                    citizenship_at_birth=self.faker.country(),
                    present_citizenship=self.faker.country(),
                    present_citizenship_not_available=self.faker.random_element(
                        elements=["Yes", "No"]
                    ),
                    provide_circumstances=self.faker.text(max_nb_chars=300),
                    parent=parent,
                    parent_address=parent_address,
                    sponsor=sponsor,
                    sponsor_address=sponsor_address,
                    is_sponsor_signed=self.faker.boolean(),
                    sponsor_date_of_signature=self.faker.date(),
                    witness=witness,
                    witness_address=waitness_address,
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully populated Citizenship for under 20 - formE data"
            )
        )
