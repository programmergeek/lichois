from random import randint

from django.db import transaction
from faker import Faker

from app.models import ApplicationDocument
from app_personal_details.models import Person, Permit
from app.utils.system_enums import ApplicationProcesses
from lichois.management.base_command import CustomBaseCommand
from workresidentpermit.models import VariationPermit
from workresidentpermit.utils import WorkResidentPermitApplicationTypeEnum


class Command(CustomBaseCommand):
    help = "Populate data for Variation Application model"
    application_type = None
    process_name = ApplicationProcesses.EXEMPTION_CERTIFICATE.value

    def handle(self, *args, **options):
        faker = Faker()
        work_res_variation_permit = (
            WorkResidentPermitApplicationTypeEnum.EXEMPTION_CERTIFICATE_VARIATION.value
        )
        
        for _ in range(50):
            self.application_type = faker.random_element(
                elements=(
                    work_res_variation_permit, 
                )
            )
            app, version = self.create_basic_data()

            permit = Permit.objects.create(
                date_issued=faker.date(),
            )

            subscriber = Person.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
            )

            VariationPermit.objects.get_or_create(
                application_version=version,
                document_number=app.application_document.document_number,
                existing_permit=permit,
                expiry_date=faker.date(),
                current_company_name=faker.company(),
                new_company_name=faker.company(),
                new_company_location=faker.address(),
                has_separate_permises=faker.random_element(
                    elements=("yes", "no")
                ),
                no_permises_reason=faker.text(),
                new_company_services_provided=faker.random_element( 
                    elements=("Technology", "Retail", "Healthcare", "Finance",
                                "Marketing", "Consulting", "Education", "Logistics")),
                current_employment_capacity=faker.job(),
                upcoming_employment_capacity=faker.job(),
                variation_for_same_employee=faker.random_element(elements=("yes", "no")),
                understudies_situation=faker.text(),
                draw_salary=faker.random_element(elements=("yes", "no")),
                salary_per_annum=faker.pydecimal(
                    left_digits=5, right_digits=2, positive=True
                ),
                new_company_employee_count=faker.random_int(min=1, max=100),
                new_company_registration=faker.date_between(
                    start_date="-10y", end_date="today"
                ),
                man_power_projection=faker.text(),
                amount_invested=faker.pydecimal(
                    left_digits=7, right_digits=2, positive=True
                ),
                initial_capital_source=faker.random_element(
                    elements=("local", "international")
                ),
                financial_institution_name=faker.company(),
                financial_institution_address=faker.address(),
                subscriber=subscriber,
                signature=f"{faker.first_name()} {faker.last_name()}",
                applicant_type=faker.random_element(
                    elements=("employee", "investor", "self employed")
                ),
            )
                

            self.stdout.write(self.style.SUCCESS("Successfully populated data"))
