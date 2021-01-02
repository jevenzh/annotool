# Generated by Django 3.1.4 on 2021-01-02 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationTasks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='task_id')),
                ('status_level', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='CaseReportFiles',
            fields=[
                ('rid', models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='record_id')),
                ('crf_path', models.CharField(max_length=600, verbose_name='crf_files_path')),
                ('is_active', models.BooleanField(default=False, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='VotedPatientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.SmallIntegerField(choices=[('male', 0), ('female', 1)], default=0)),
                ('age', models.SmallIntegerField()),
                ('height', models.SmallIntegerField()),
                ('weight', models.SmallIntegerField()),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotask.casereportfiles')),
            ],
        ),
        migrations.CreateModel(
            name='VotedAnnotations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('category', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=20)),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotask.casereportfiles')),
            ],
        ),
        migrations.CreateModel(
            name='UserPatientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.SmallIntegerField(choices=[('male', 0), ('female', 1)], default=0)),
                ('age', models.SmallIntegerField()),
                ('height', models.SmallIntegerField()),
                ('weight', models.SmallIntegerField()),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotask.annotationtasks')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnnotations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('category', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=20)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotask.annotationtasks')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='annotationtasks',
            name='rid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotask.casereportfiles'),
        ),
        migrations.AddField(
            model_name='annotationtasks',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
