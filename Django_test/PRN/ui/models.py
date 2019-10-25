# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from unittest.util import _MAX_LENGTH

# Create your models here.

class School(models.Model):
    inst_choices=(
        ('P','Primary'),
        ('S', 'Secondary'),
        ('U','Univercity'),
        )
    
    name=models.CharField(max_length=253)
    institution=models.CharField(max_length=10, choices=inst_choices)
    location=models.CharField(max_length=253)
    
    def __str__(self):
        
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=253)
    section=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    home=models.CharField(max_length=253)
    school=models.ForeignKey(School)
    
    def __str__(self):
        return self.name
    
    

class Note(models.Model):
    notes=models.CharField(max_length=253)
    student=models.ForeignKey(Student)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.student.name + ":" + self.notes + ":" + str(self.created)
    