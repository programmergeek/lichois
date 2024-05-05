from rest_framework import serializers
from ..models import AssessmentResult


class AssessmentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentResult
        fields = ['id', 'score', 'output_results', 'result_date']
