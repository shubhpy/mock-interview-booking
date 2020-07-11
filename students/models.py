from django.db import models
from system_config.models import SystemConfig


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    free_mock_interviews_allowed = models.IntegerField(default=0)
    free_mock_interviews_availed = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            systemconfig = SystemConfig.objects.first()
            if systemconfig and hasattr(systemconfig, 'students_free_mock_interviews_allowed'):
                self.free_mock_interviews_allowed = systemconfig.students_free_mock_interviews_allowed
        return super(Student, self).save(*args, **kwargs)
