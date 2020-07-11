from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from interviewers.models import Interviewer, InterviewerSlot
from interviewers.serializers import InterviewerSerializer, InterviewerSlotSerializer, \
    AvailableInterviewerSlotsRequestConsumer, BookInterviewerSlotRequestConsumer
from students.models import Student
from interviews.models import Interview


class InterviewerViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Interviewer.objects
    serializer_class = InterviewerSerializer
    http_method_names = ['get', 'post', 'put']


class InterviewerSlotViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = InterviewerSlot.objects
    serializer_class = InterviewerSlotSerializer
    http_method_names = ['get', 'post', 'put']

    @action(methods=['POST'], detail=False, url_path="available")
    def available(self, request, *args, **kwargs):
        consumer = AvailableInterviewerSlotsRequestConsumer(data=request.data)
        if consumer.is_valid(raise_exception=True):
            student_id = consumer.validated_data['student_id']
            start_date_time = consumer.validated_data['start_date_time']
            end_date_time = consumer.validated_data['end_date_time']

            student = Student.objects.filter(id=student_id).first()
            if not student:
                return Response({"msg": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
            if student.free_mock_interviews_availed == student.free_mock_interviews_allowed:
                return Response({"msg": "Student availed all free mocks"}, status=status.HTTP_400_BAD_REQUEST)

            last_2_completed_interviews = Interview.objects.filter(student_id=student_id, status=Interview.COMPLETED).order_by('-interviewerslot_id__end_date_time')[:2]
            for interview in last_2_completed_interviews:
                if interview.grades <= 1:
                    return Response({"msg": "Sorry, Your one of last two grades are < 1"}, status=status.HTTP_400_BAD_REQUEST)

            student_interviewed_with = list(set(list(Interview.objects.filter(student_id=student_id).values_list('interviewerslot_id__id', flat=True))))
            available_slots = self.get_queryset().exclude(interviewer_id__id__in=student_interviewed_with).filter(active=True, start_date_time__gte=start_date_time, end_date_time__lte=end_date_time)
            serializer = self.get_serializer(available_slots, many=True)
            return Response(serializer.data)

    @action(methods=['POST'], detail=False, url_path="book")
    def book(self, request, *args, **kwargs):
        consumer = BookInterviewerSlotRequestConsumer(data=request.data)
        if consumer.is_valid(raise_exception=True):
            student_id = consumer.validated_data['student_id']
            interviewer_slot_id = consumer.validated_data['interviewer_slot_id']

            student = Student.objects.filter(id=student_id).first()
            if not student:
                return Response({"msg": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
            interviewer_slot = self.get_queryset().filter(id=interviewer_slot_id, active=True).first()
            if not interviewer_slot:
                return Response({"msg": "Active Interviewer Slot not found"}, status=status.HTTP_404_NOT_FOUND)
            student.free_mock_interviews_availed += 1
            student.save()

            interviewer_slot.active = False
            interviewer_slot.save()

            new_interview = Interview(
                student_id=student,
                interviewerslot_id=interviewer_slot,
                interviewer_id=interviewer_slot.interviewer_id
            )
            new_interview.save()

            serializer = self.get_serializer(interviewer_slot)
            return Response({"msg": "Slot Booked", "data": serializer.data})
