# Generated by Django 3.0.8 on 2020-07-11 21:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('interviewers', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mock', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('booked', 'booked'), ('cancelled', 'cancelled'), ('completed', 'completed')], default='booked', max_length=30)),
                ('grades', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('interviewer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='interviewers.Interviewer')),
                ('interviewerslot_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='interviewers.InterviewerSlot')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='students.Student')),
            ],
        ),
    ]
