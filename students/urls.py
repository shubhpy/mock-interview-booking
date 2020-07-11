from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from students.views import StudentViewSet

router = routers.SimpleRouter()
router.register(r'', StudentViewSet, basename='students')
urlpatterns = [
    url(r'', include(router.urls))
]