import django_filters

from rest_framework import viewsets

from ..api.serializers import AssessmentResultSerializer, AssessmentSerializer
from ..models import AssessmentResult, Assessment


class AssessmentResultModelFilter(django_filters.FilterSet):

    document_number = django_filters.CharFilter(
        document_number='document_number', lookup_expr='exact')

    min_result_date = django_filters.DateFilter(field_name='created', lookup_expr='gte')
    max_result_date = django_filters.DateFilter(field_name='created', lookup_expr='lte')

    class Meta:
        model = AssessmentResult
        exclude = ('user_created', 'output_results')


class AssessmentModelFilter(django_filters.FilterSet):

    document_number = django_filters.CharFilter(
        document_number='document_number', lookup_expr='exact')

    min_result_date = django_filters.DateFilter(field_name='created', lookup_expr='gte')
    max_result_date = django_filters.DateFilter(field_name='created', lookup_expr='lte')

    class Meta:
        model = Assessment
        exclude = ('user_created', 'marking_score')


class AssessmentResultViewSet(viewsets.ModelViewSet):
    queryset = AssessmentResult.objects.all()
    serializer_class = AssessmentResultSerializer
    filterset_class = AssessmentResultModelFilter


class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    filterset_class = AssessmentModelFilter
