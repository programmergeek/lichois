from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api.viewsets.production_attachment_document_viewset import (
    ProductionAttachmentDocumentDownloadView,
)
from .api.viewsets import ProductionPermitView, TravelCertificateProductionPermitView

urlpatterns = [
    path(
        "production/<str:document_number>",
        ProductionPermitView.as_view(),
        name="production-permit",
    ),
    path(
        "travel/production/<str:document_number>",
        TravelCertificateProductionPermitView.as_view(),
    ),
    path(
        'production-download/<str:document_number>/',
        ProductionAttachmentDocumentDownloadView.as_view(),
    ),
]
