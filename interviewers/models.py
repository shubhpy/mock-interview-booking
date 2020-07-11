from django.db import models


class Interviewer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InterviewerSlot(models.Model):
    interviewer_id = models.ForeignKey(Interviewer, on_delete=models.PROTECT)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
