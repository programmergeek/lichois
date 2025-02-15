from django.apps import apps
from ..api import CitizenshipBySettlementApplication
from app_personal_details.models import Person
from app_address.models import ApplicationAddress
from app_attachments.models import ApplicationAttachment
from app_contact.models import ApplicationContact
from ..models import PersonalDeclaration, DCCertificate, CitizenshipBySettlement


class CitizenshipBySettlementData(object):

	def __init__(self, document_number):
		self.document_number = document_number
		self.citizenship_by_settlement_application = CitizenshipBySettlementApplication()

	def data(self):
		return self.prepare()

	def prepare(self):
		self.citizenship_by_settlement_application.personal_details = self.personal_details
		self.citizenship_by_settlement_application.contacts = self.contacts()
		self.citizenship_by_settlement_application.address = self.address()
		self.citizenship_by_settlement_application.personal_declaration = self.personal_declaration()
		self.citizenship_by_settlement_application.dc_certificate = self.dc_certificate()
		self.citizenship_by_settlement_application.citizenship_by_settlement = self.citizenship_by_settlement()
		return self.citizenship_by_settlement_application

	def personal_details(self):
		"""
		TODO: review the join, may result in slow system.
        """
		return self.get_model_class(Person._meta.app_label.lower())

	def address(self):
		return self.get_model_class(ApplicationAddress._meta.app_label.lower())

	def contacts(self):
		return self.get_model_class(ApplicationContact._meta.app_label.lower())

	def personal_declaration(self):
		return self.get_model_class(PersonalDeclaration._meta.app_label.lower())

	def dc_certificate(self):
		return self.get_model_class(DCCertificate._meta.app_label.lower())

	def citizenship_by_settlement(self):
		return self.get_model_class(CitizenshipBySettlement._meta.app_label.lower())

	# def personal_declaration(self):
	# 	return self.get_model_class(ApplicationContact._meta.app_label.lower())
	# 	"""
	# 	"""#TODO: define the relationship for onetomany, foreignkey?
	# 	# residential_histories = ResidentialHistory.objects.filter(
	# 	# 	work_resident_permit__document_number=self.document_number)
	# 	return #residential_histories

	# def attachments(self):
	# 	attachments = ApplicationAttachment.objects.filter(
	# 		application_version__application__application_document__document_number=self.document_number)
	# 	return attachments

	def get_model_class(self, model_string):
		try:
			app_label, model_name = model_string.split('.')
			model_cls = apps.get_model(app_label, model_name)
		except ValueError:
			raise ValueError("Model string must be in the format 'app_label.ModelName'")
		except LookupError:
			raise LookupError(f"Model '{model_string}' not found")
		else:
			try:
				form_details = model_cls.objects.get(document_number=self.document_number)
				return form_details
			except model_cls.DoesNotExist:
				pass
