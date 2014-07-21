from django import forms
from student.models import WeeklyExpenses

class StudentForm(forms.Form):
   name = forms.CharField(max_length=30)
