# Generated by Django 5.0 on 2024-10-31 00:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.URLField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('online', 'Online Exam'), ('class', 'Class Exam'), ('missed', 'Missed Exam')], max_length=10)),
                ('date_joined', models.DateField()),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('student_type', models.CharField(choices=[('member', 'Member'), ('non-member', 'Non-member')], max_length=10)),
                ('cohort_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='cohorts.cohort')),
                ('program_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='cohorts.program')),
            ],
        ),
    ]
