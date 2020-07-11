from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from students.models import Student
from students.serializers import StudentSerializer
from system_config.models import SystemConfig


class StudentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Student.objects
    serializer_class = StudentSerializer
    http_method_names = ['get', 'post', 'put']
