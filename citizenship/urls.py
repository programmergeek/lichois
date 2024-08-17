from django.urls import path, include
from django.urls.conf import path
from rest_framework.routers import DefaultRouter

from .admin_site import citizenship_admin
from .views.board import (BoardModelViewSet, MeetingViewSet, ScoreSheetViewSet, MeetingSessionViewSet, \
                          ConflictOfInterestViewSet, ConflictOfInterestDurationViewSet, BatchModelViewSet,
                          InterviewResponseViewSet, \
                          AttendeeViewSet, BoardMemberViewSet, BatchApplicationViewSet)

from .views.board.interview_viewset import InterviewViewSet
from .views.summary import (RenunciationSummaryViewSet, AdoptedChildSummaryViewSet, PresPower10ASummaryViewSet,
                            PresPower10BSummaryViewSet, IntentionNaturalizationFSSummaryViewSet,
                            MaturityPeriodWaiverSummaryViewSet, DualRenunciationSummaryViewSet)

app_name = 'citizenship'

router = DefaultRouter()
router.register(r'citizenship-boards', BoardModelViewSet)
router.register(r'citizenship-meetings', MeetingViewSet, basename='meeting')
router.register(r'citizenship-meeting-sessions', MeetingSessionViewSet)
router.register(r'citizenship-scoresheets', ScoreSheetViewSet)
router.register(r'citizenship-conflict-of-interests', ConflictOfInterestViewSet)
router.register(r'citizenship-conflict-of-interest-durations', ConflictOfInterestDurationViewSet)
router.register(r'citizenship-batches', BatchModelViewSet, basename='batch')
router.register(r'citizenship-interview-responses', InterviewResponseViewSet)
router.register(r'citizenship-meeting-attendees', AttendeeViewSet)
router.register(r'citizenship-boardmembers', BoardMemberViewSet),
router.register(r'citizenship-batch-applications', BatchApplicationViewSet)
router.register(r'citizenship-interviews', InterviewViewSet, basename='interview')
router.register(r'citizenship-renunciation-summary', RenunciationSummaryViewSet, basename='renunciation')
router.register(r'citizenship-adopted-child-summary', AdoptedChildSummaryViewSet, basename='adopted-child')
router.register(r'citizenship-pre-10a-summary', PresPower10ASummaryViewSet, basename='pre-10a')
router.register(r'citizenship-pre-10b-summary', PresPower10BSummaryViewSet, basename='pre-10b')
router.register(r'citizenship-intention-naturalization', IntentionNaturalizationFSSummaryViewSet,
                basename='intention-naturalization')
router.register(r'citizenship-maturity-waiver', MaturityPeriodWaiverSummaryViewSet, basename='maturity-waiver')
router.register(r'citizenship-dual-renunciation', DualRenunciationSummaryViewSet, basename='dual-renunciation')


urlpatterns = [
    path('admin/', citizenship_admin.urls),
    path('', include(router.urls)),
]
