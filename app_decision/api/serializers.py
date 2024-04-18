from rest_framework import serializers

from app_decision.models import ApplicationDecision, ApplicationDecisionType


class ApplicationDecisionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicationDecisionType
        fields = (
            'code',
            'name',
            'process_types',
            'valid_from',
            'valid_to'
        )


class ApplicationDecisionSerializer(serializers.ModelSerializer):

    decision_type = ApplicationDecisionTypeSerializer()

    proposed_decision_type = ApplicationDecisionTypeSerializer()

    class Meta:
        model = ApplicationDecision
        fields = (
            'decision_type',
            'proposed_decision_type',
            'description',
            'application_document'
        )
