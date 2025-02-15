from django.views.generic.base import RedirectView
from .admin_site import board_admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicationBatchCreateView
from .viewsets import (
    AgendaViewSet,
    AgendaItemViewSet,
    BoardMeetingViewSet,
    ApplicationBatchViewSet,
    MeetingAttendeeViewSet,
    BoardMeetingVoteViewSet,
    BoardDecisionViewSet,
    VotingProcessViewSet,
    InterestDeclarationViewSet,
    MeetingInvitationViewSet,
)

app_name = "board"
router = DefaultRouter()
router.register(r"agendas", AgendaViewSet, basename="agendas")
router.register(r"agenda-items", AgendaItemViewSet, basename="agenda-items")
router.register(r"board-meetings", BoardMeetingViewSet, basename="board-meetings")
router.register(
    r"application-batches", ApplicationBatchViewSet, basename="application-batches"
)
router.register(
    r"meeting-attendees", MeetingAttendeeViewSet, basename="meeting-attendees"
)
router.register(
    r"board-decision-votes", BoardMeetingVoteViewSet, basename="board-decision-votes"
)
router.register(r"board-decisions", BoardDecisionViewSet, basename="board-decisions")
router.register(
    r"interest-declarations",
    InterestDeclarationViewSet,
    basename="interest-declarations",
)
router.register(
    r"meeting_invitations", MeetingInvitationViewSet, basename="meeting-invitations"
)
router.register(r"voting-process", VotingProcessViewSet, basename="voting-process")


urlpatterns = [
    path("board/", board_admin.urls),
    path(
        "application-batches/create",
        ApplicationBatchCreateView.as_view(),
        name="application-batch-create",
    ),
    path("", RedirectView.as_view(url="admin/"), name="home_url"),
    path("", include(router.urls)),
]
