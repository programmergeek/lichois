import logging

from django.dispatch import receiver
from django.db.models.signals import post_save

from app.utils import ApplicationDecisionEnum

from workresidentpermit.models import WorkPermit, SecurityClearance
from app_decision.models import ApplicationDecision
from workresidentpermit.classes import WorkResidentPermitApplicationDecisionService

from app.utils import ApplicationStatuses
from .tasks import async_production

from .classes import WorkPermitApplicationPDFGenerator

logger = logging.getLogger(__name__)


@receiver(post_save, sender=WorkPermit)
def generate_pdf_summary(sender, instance, created, **kwargs):
    try:
        if sender.application_version.application.application_status.name in \
                [ApplicationStatuses.VERIFICATION.value,
                 ApplicationStatuses.CANCELLED.value,
                 ApplicationStatuses.REJECTED.value,
                 ApplicationStatuses.ACCEPTED.value]:
            generator = WorkPermitApplicationPDFGenerator(work_resident_permit=sender)
            generator.generate()
    except SystemError as e:
        logger.debug("SystemError: An error occurred while generating the PDF, Got ", e)
    except Exception as ex:
        logger.debug("An error occurred while generating the PDF, Got ", ex)


@receiver(post_save, sender=SecurityClearance)
def create_application_decision(sender, instance, created, **kwargs):
    try:
        if created:
            service = WorkResidentPermitApplicationDecisionService(
                document_number=instance.document_number,
                security_clearance=instance
            )
            service.create()
    except SystemError as e:
        logger.error("SystemError: An error occurred while creating new application decision, Got ", e)
    except Exception as ex:
        logger.error(f"An error occurred while trying to create application decision after saving board decision. "
                     f"Got {ex} ")


@receiver(post_save, sender=ApplicationDecision)
def create_production_pdf(sender, instance, created, **kwargs):
    try:
        if created:
            if instance.final_decision_type.code.lower() == ApplicationDecisionEnum.APPROVED.value.lower():
                async_production(document_number=instance.document_number)
    except SystemError as e:
        logger.error("SystemError: An error occurred while creating production pdf ", e)
    except Exception as ex:
        logger.error(f"An error occurred while trying to creating a production pdf "
                     f"Got {ex} ")
        


