import django_filters

from app.models import Application


class ApplicationModelFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(
        field_name='application_document__applicant__full_name', lookup_expr='icontains')

    batched = django_filters.BooleanFilter(field_name='batched')

    security_clearance = django_filters.CharFilter(field_name='security_clearance')

    board = django_filters.CharFilter(field_name='board')

    verification = django_filters.CharFilter(field_name='verification')

    assessment = django_filters.CharFilter(field_name='assessment')

    gazette = django_filters.CharFilter(field_name='gazette')

    application_document_number = django_filters.CharFilter(
        field_name='application_document__document_number', lookup_expr='icontains')
    application_status = django_filters.CharFilter(
        field_name='application_status__code', lookup_expr='icontains')
    min_created_date = django_filters.DateFilter(field_name='created', lookup_expr='gte')
    max_created_date = django_filters.DateFilter(field_name='created', lookup_expr='lte')

    class Meta:
        model = Application
        exclude = ('last_application_version_id',)
