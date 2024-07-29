from django.urls import path, include

from rest_framework.routers import DefaultRouter

from app_assessment.views import (
    AssessmentResultViewSet,
    AssessmentViewSet,
    NewAssessmentInvestorViewSet,
    AssessmentEmergencyViewSet,
    RenewalAssessmentInvestorViewSet,
    AssessmentCaseNoteViewSet,
    AssessmentCaseSummaryViewSet,
    AssessmentCaseDecisionViewSet,
    BlueCardAssessmentViewSet,
)

from app_assessment.views.appeal_assessment_viewset import AppealAssessmentViewSet
from app_assessment.views.assessment_case_decision_apiview import (
    AssessmentCaseDecisionAPIView,
)
from app_assessment.views.dependant_assessment_viewset import DependantAssessmentViewSet

router = DefaultRouter()
router.register(r"assessments", AssessmentViewSet)
router.register(r"new_assessment_investors", NewAssessmentInvestorViewSet)
router.register(r"renewal_assessment_investors", RenewalAssessmentInvestorViewSet)
router.register(r"assessment-emergency", AssessmentEmergencyViewSet)
router.register(r"assessment-appeal", AppealAssessmentViewSet)
router.register(r"dependant-assessment", DependantAssessmentViewSet)
router.register(r"assessment-results", AssessmentResultViewSet)
router.register(r"assessment-notes", AssessmentCaseNoteViewSet)
router.register(r"assessment-case-summary", AssessmentCaseSummaryViewSet)
router.register(r"blue-card-assessment", BlueCardAssessmentViewSet)
# router.register(r'assessment-case-decision', AssessmentCaseDecisionViewSet)

urlpatterns = [
    path(
        "assessment-case-decision/",
        AssessmentCaseDecisionAPIView.as_view(),
        name="assessmentcasedecision",
    ),
    path("", include(router.urls)),
]
