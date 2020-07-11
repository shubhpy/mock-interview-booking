from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from interviews.models import Interview
from interviews.serializers import InterviewSerializer, MarkInterviewCompleteConsumer


class InterviewViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Interview.objects
    serializer_class = InterviewSerializer
    http_method_names = ['get', 'post']

    @action(methods=['POST'], detail=True, url_path="complete")
    def complete(self, request, pk, *args, **kwargs):
        self.get_object()
        interview = self.get_queryset().filter(id=pk, status=Interview.BOOKED).first()
        if not interview:
            return Response(status=status.HTTP_404_NOT_FOUND)

        consumer = MarkInterviewCompleteConsumer(interview, data=request.data)
        consumer.is_valid(raise_exception=True)
        consumer.save()
        interview.complete()
        return Response(consumer.data)
