from django.contrib import admin
from django.contrib.auth.admin import *

# Register your models here.
from student.models import WeeklyExpenses
admin.site.register(WeeklyExpenses)
