from django.utils import timezone

from rest_framework import serializers

from app.api.serializers import ApplicationSerializer
from authentication.serializers import UserSerializer
from board.models import BoardMember
from citizenship.models import Meeting, Attendee, Batch, BatchApplication, Board, Question, Interview, \
    InterviewDecision, ScoreSheet, Role, ConflictOfInterest, InterviewResponse
from citizenship.models.board.board_recommandation import BoardRecommendation
from citizenship.models.board.conflict_of_interest_duration import ConflictOfInterestDuration
from citizenship.models.board.interview_question import InterviewQuestion
from citizenship.models.board.meeting_session import MeetingSession


class MeetingSerializer(serializers.ModelSerializer):

    start_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S%z", input_formats=["%Y-%m-%dT%H:%M:%S%z", "iso-8601"])
    end_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S%z", input_formats=["%Y-%m-%dT%H:%M:%S%z", "iso-8601"])

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if start_date and start_date.tzinfo is None:
            data['start_date'] = timezone.make_aware(start_date)
        if end_date and end_date.tzinfo is None:
            data['end_date'] = timezone.make_aware(end_date)

        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError("End date must be after start date.")

        return data

    class Meta:
        model = Meeting
        fields = '__all__'


class MeetingSessionSerializer(serializers.ModelSerializer):

    meeting = serializers.PrimaryKeyRelatedField(queryset=Meeting.objects.all(), required=False, allow_null=True)

    class Meta:
        model = MeetingSession
        fields = '__all__'


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'


class BatchApplicationCitizenshipSerializer(serializers.ModelSerializer):
    batch = BatchSerializer()
    application = ApplicationSerializer()
    meeting_session = MeetingSessionSerializer()

    class Meta:
        model = BatchApplication
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class InterviewQuestionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = InterviewQuestion
        fields = '__all__'


# class InterviewSerializer(serializers.ModelSerializer):
#     questions = InterviewQuestionSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Interview
#         fields = '__all__'
class InterviewSerializer(serializers.ModelSerializer):

    meeting_session = MeetingSessionSerializer()

    class Meta:
        model = Interview
        fields = '__all__'


class InterviewDecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewDecision
        fields = '__all__'


class ScoreSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreSheet
        fields = '__all__'


class BoardRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardRecommendation
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class InterviewQuestionCSVSerializer(serializers.Serializer):
    csv_file = serializers.FileField()


class ConflictOfInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConflictOfInterest
        fields = '__all__'


class ConflictOfInterestDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConflictOfInterestDuration
        fields = '__all__'


class BoardMemberCitizenshipSerializer(serializers.ModelSerializer):

    board = BoardSerializer()
    user = UserSerializer()

    class Meta:
        model = BoardMember
        fields = '__all__'


class InterviewResponseSerializer(serializers.ModelSerializer):
    interview = InterviewSerializer(read_only=True)  # Make interview read-only
    member = BoardMemberCitizenshipSerializer(read_only=True)  # Make member read-only

    class Meta:
        model = InterviewResponse
        fields = '__all__'
        read_only_fields = [
            'interview',
            'member',
            'text',
            'marks_range',
            'category',
            'sequence'
        ]

    def update(self, instance, validated_data):
        instance.score = validated_data.get('score', instance.score)
        instance.is_marked = validated_data.get('is_marked', instance.is_marked)
        instance.additional_comments = validated_data.get('response', instance.response)
        instance.additional_comments = validated_data.get('additional_comments', instance.additional_comments)
        instance.save()
        return instance

