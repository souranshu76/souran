# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import School, Student, Note

# Register your models here.


admin.site.register(School)
admin.site.register(Student)
admin.site.register(Note)