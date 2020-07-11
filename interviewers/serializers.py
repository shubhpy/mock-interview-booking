from rest_framework import serializers
from interviewers.models import Interviewer, InterviewerSlot


class InterviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviewer
        fields = '__all__'


class InterviewerSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewerSlot
        fields = '__all__'


class AvailableInterviewerSlotsRequestConsumer(serializers.Serializer):
    student_id = serializers.IntegerField(required=True)
    start_date_time = serializers.DateTimeField(required=True)
    end_date_time = serializers.DateTimeField(required=True)


class BookInterviewerSlotRequestConsumer(serializers.Serializer):
    student_id = serializers.IntegerField(required=True)
    interviewer_slot_id = serializers.IntegerField(required=True)
