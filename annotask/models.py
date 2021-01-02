from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CaseReportFiles(models.Model):
    rid = models.CharField(max_length=200, verbose_name="record_id", primary_key=True)
    crf_path = models.CharField(max_length=600, verbose_name="crf_files_path")
    is_active = models.BooleanField(default=False, verbose_name="")


class AnnotationTasks(models.Model):
    id = models.AutoField(verbose_name='task_id', primary_key=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    rid = models.ForeignKey(CaseReportFiles, on_delete=models.CASCADE)
    status_level = models.FloatField(default=0.)


class UserAnnotations(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    task_id = models.ForeignKey(AnnotationTasks, on_delete=models.CASCADE)
    
    start_time = models.TimeField()
    end_time = models.TimeField()
    category = models.CharField(max_length=50)
    value = models.CharField(max_length=20)


class UserPatientInfo(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    task_id = models.ForeignKey(AnnotationTasks, on_delete=models.CASCADE)

    name = models.CharField(max_length=20)
    gender = models.SmallIntegerField(default=0, choices=(("male", 0), ("female", 1)))
    age = models.SmallIntegerField()
    height = models.SmallIntegerField()
    weight = models.SmallIntegerField()


class VotedAnnotations(models.Model):
    rid = models.ForeignKey(CaseReportFiles, on_delete=models.CASCADE)
    
    start_time = models.TimeField()
    end_time = models.TimeField()
    category = models.CharField(max_length=50)
    value = models.CharField(max_length=20)


class VotedPatientInfo(models.Model):
    rid = models.ForeignKey(CaseReportFiles, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=20)
    gender = models.SmallIntegerField(default=0, choices=(("male", 0), ("female", 1)))
    age = models.SmallIntegerField()
    height = models.SmallIntegerField()
    weight = models.SmallIntegerField()