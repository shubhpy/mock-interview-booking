from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from system_config.models import SystemConfig
from system_config.serializers import SystemConfigSerializer


class SystemConfigViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = SystemConfig.objects
    serializer_class = SystemConfigSerializer
    http_method_names = ['get', 'post', 'put']

    def create(self, request, *args, **kwargs):
        if self.get_queryset().count():
            return Response({"msg": "Config Exists"}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
