from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from system_config.views import SystemConfigViewSet

router = routers.SimpleRouter()
router.register(r'^systemconfig', SystemConfigViewSet, basename='systemconfig')
urlpatterns = [
    url(r'^', include(router.urls))
]