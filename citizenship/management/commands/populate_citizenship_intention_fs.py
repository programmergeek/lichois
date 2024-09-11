from django.db.transaction import atomic
from model_bakery import baker


from app_personal_details.models import Person
from lichois.management.base_command import CustomBaseCommand
from ...utils import CitizenshipProcessEnum, CitizenshipApplicationTypeEnum
from ...models import DeclarationNaturalisationByForeignSpouse, ResidentialHistory, OathOfAllegiance


class Command(CustomBaseCommand):
    help = "Populate data for registration of adopted child over 3 years old service"
    process_name = CitizenshipProcessEnum.INTENTION_FOREIGN_SPOUSE.value
    application_type = (
        CitizenshipApplicationTypeEnum.INTENTION_FOREIGN_SPOUSE_ONLY.value
    )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(f"Process name {self.process_name}"))

        for _ in range(50):

            with atomic():
                fname = self.faker.unique.first_name()
                lname = self.faker.unique.last_name()

                # new_application
                app, version = self.create_new_application(fname, lname)

                self.create_basic_data()

                # Residential History
                baker.make(
                    ResidentialHistory,
                    application_version=version,
                    document_number=app.application_document.document_number,
                )

                # TODO: PersonalDeclaration

                # Applicant Oath
                baker.make(
                    OathOfAllegiance,
                    application_version=version,
                    document_number=app.application_document.document_number,
                )

                # declarant_personal_info
                baker.make(
                    Person,
                    application_version=version,
                    document_number=app.application_document.document_number,
                    person_type="declarant",
                )

                # Declarant Citizenship details
                baker.make(DeclarationNaturalisationByForeignSpouse)

                # declarant preferred contact
                self.create_application_contact(app, version)

                self.stdout.write(
                    self.style.SUCCESS(
                        "Successfully populated citizenship intention by foreign spouse data"
                    )
                )
