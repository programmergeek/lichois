import os

from django.test import TestCase

from app_assessment.models import Assessment
from app_assessment.validators import AssessmentValidator

from app_checklist.utils import ReadJSON


class TestAssessmentInvestorValidator(TestCase):

    """
        "business_activity": 10,
        "equity_investment": 15,
        "total_investment": 25,
        "number_of_batswana_employees": 30,
        "proportion_partners": 40,
        "investor_or_entrepreneur": 30,
        "maximum_points": 135,
        "pass_mark": 81
    """
    def setUp(self):

        file_name = "marking_score_work_and_residence_investor.json"
        self.config_location = os.path.join(os.getcwd(), "app_assessment", "data", "assessments", file_name)
        #self.assessment = AssessmentInvestor()
        self.assessment.business_activity = 40
        self.assessment.equity_investment = 10
        self.assessment.number_of_batswana_employees = 5
        self.assessment.investor_or_entrepreneur = 5
        self.assessment.proportion_partners = 20

        reader = ReadJSON(file_location=self.config_location)
        self.validator = AssessmentValidator(
            assessment=self.assessment,
            rules=reader.json_data()
        )

    def test_validate_main_sections_invalid(self):
        self.validator.validate_main_sections()
        self.assertFalse(self.validator.is_valid())
        self.assertGreater(len(self.validator.response.messages), 0)

    def test_validate_main_sections_valid(self):
        self.assessment.qualification = 10
        self.validator.validate_main_sections()
        self.assertTrue(self.validator.is_valid())

    def test_validate_main_sections_valid(self):
        self.assessment.total = 135
        self.assertFalse(self.validator.is_valid())
