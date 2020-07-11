from rest_framework import serializers
from interviews.models import Interview


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'


class MarkInterviewCompleteConsumer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ('grades', 'completed_at', 'note')
