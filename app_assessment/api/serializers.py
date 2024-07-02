import os

from rest_framework import serializers

from app_checklist.utils import ReadJSON
from ..models import AssessmentResult, AssessmentInvestor
from app_assessment.models import Assessment, AssessmentEmergency
from app_assessment.validators import AssessmentValidator


class AssessmentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentResult
        fields = ['id', 'score', 'output_results', 'result_date']


class AssessmentSerializer(serializers.ModelSerializer):

    document_number = serializers.CharField(required=True)

    def validate(self, data):

        file_name = "marking_score_work_and_residence.json"
        file_location = os.path.join(os.getcwd(), "app_assessment", "data", "assessments", file_name)
        reader = ReadJSON(file_location=file_location)

        assessment = Assessment(**data)
        validator = AssessmentValidator(assessment=assessment, rules=reader.json_data())
        if not validator.is_valid():
            raise serializers.ValidationError(validator.response.result())

        return data

    class Meta:
        model = Assessment
        fields = ['id', 'competency', 'qualification', 'employer_justification', 'scarce_skill', 'work_experience',
                  'total', 'score', 'marking_score', 'document_number']


class AssessmentInvestorSerializer(serializers.ModelSerializer):

    document_number = serializers.CharField(required=True)

    def validate(self, data):

        file_name = "marking_score_work_and_residence_investor.json"
        file_location = os.path.join(os.getcwd(), "app_assessment", "data", "assessments", file_name)
        reader = ReadJSON(file_location=file_location)

        assessment = AssessmentInvestor(**data)
        validator = AssessmentValidator(assessment=assessment, rules=reader.json_data())
        if not validator.is_valid():
            raise serializers.ValidationError(validator.response.result())

        return data

    class Meta:
        model = AssessmentInvestor
        fields = '__all__'


class AssessmentEmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentEmergency
        fields = '__all__'
