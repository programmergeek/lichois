from django.db import models
import uuid

from base_module.model_mixins import BaseUuidModel

from .permissions import BoardBasePermissionModel
from .board_meeting import BoardMeeting
from .board_member import BoardMember
from ..choices import MEETING_INVITATION_STATUS


class MeetingInvitation(BaseUuidModel, BoardBasePermissionModel):
    board_meeting = models.ForeignKey(BoardMeeting, on_delete=models.CASCADE)
    invited_user = models.ForeignKey(
        BoardMember,
        on_delete=models.CASCADE,
        related_name="received_invitations",
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=MEETING_INVITATION_STATUS,
        default="pending",
    )  # Possible values:
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Invitation to {self.invited_user} for {self.board_meeting}"
