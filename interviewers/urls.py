from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from interviewers.views import InterviewerViewSet, InterviewerSlotViewSet


router = routers.SimpleRouter()
router.register(r'users', InterviewerViewSet, basename='interviewrs')
router.register(r'slots', InterviewerSlotViewSet, basename='interviewrsslots')
urlpatterns = [
    url(r'', include(router.urls))
]