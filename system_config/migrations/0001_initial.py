# Generated by Django 3.0.8 on 2020-07-11 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students_free_mock_interviews_allowed', models.IntegerField(default=0)),
            ],
        ),
    ]
