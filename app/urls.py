from django.urls import path, include

from rest_framework.routers import DefaultRouter

from app.views import (
    ApplicationListView,
    ApplicationCreateView,
    ApplicationStatusViewSet,
    ApplicationVerificationCreateListView,
    ApplicationRenewalView,
    ApplicationRenewalHistoryView,
    ApplicationVerificationAPIView,
    SecurityClearanceCreateAPIView,
)

router = DefaultRouter()

router.register(r"applications", ApplicationListView)
router.register(r"application_statuses", ApplicationStatusViewSet)
router.register(r"application_verifications", ApplicationVerificationCreateListView)
router.register(r"application_renewal_history", ApplicationRenewalHistoryView)

urlpatterns = [
    path("applications", ApplicationCreateView.as_view(), name="application-new"),
    path(
        "applications/renewal",
        ApplicationRenewalView.as_view(),
        name="application-renewal",
    ),
    path("", include(router.urls)),
    path(
        "app/verification/<str:document_number>/submit/",
        ApplicationVerificationAPIView.as_view(),
        name="submit-verification",
    ),
    path(
        "security_clearance/<str:document_number>/submit/",
        SecurityClearanceCreateAPIView.as_view(),
        name="submit-security-clearance",
    ),
]
