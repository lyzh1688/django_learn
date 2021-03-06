from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    isFullTime = models.BooleanField(default=True)

class Course(models.Model):
    name = models.CharField(max_length=30)

class Class(models.Model):
    teacher = models.ForeignKey('Teacher',related_name="ClassTeacher")
    course = models.ForeignKey('Course')
    fee = models.DecimalField(max_digits=6, decimal_places=2)

class Record(models.Model):
    clazz = models.ForeignKey('Class')
    times = models.DecimalField(max_digits=2, decimal_places=0)
    date = models.CharField(max_length=6,default='201601')