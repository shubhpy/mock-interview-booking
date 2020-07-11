from django.db import models

class SystemConfig(models.Model):
    students_free_mock_interviews_allowed = models.IntegerField(default=0)

    objects = models.Manager()
