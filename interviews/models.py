from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from students.models import Student
from interviewers.models import Interviewer, InterviewerSlot


class Interview(models.Model):
    BOOKED = 'booked'
    CANCELLED = 'cancelled'
    COMPLETED = 'completed'

    STATUSES = (
        (BOOKED, 'booked'),
        (CANCELLED, 'cancelled'),
        (COMPLETED, 'completed'),
    )

    student_id = models.ForeignKey(Student, on_delete=models.PROTECT)
    interviewer_id = models.ForeignKey(Interviewer, on_delete=models.PROTECT)
    interviewerslot_id = models.ForeignKey(InterviewerSlot, on_delete=models.PROTECT)
    mock = models.BooleanField(default=True)
    status = models.CharField(choices=STATUSES, default=BOOKED, max_length=30)
    grades = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(5), MinValueValidator(0)])
    note = models.CharField(blank=True, null=True, max_length=200)
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def complete(self):
        self.status = self.__class__.COMPLETED
        self.save()
