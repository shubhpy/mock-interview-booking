from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from interviews.views import InterviewViewSet

router = routers.SimpleRouter()
router.register(r'', InterviewViewSet, basename='interviews')
urlpatterns = [
    url(r'', include(router.urls))
]