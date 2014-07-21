from django import forms
from student.models import WeeklyExpenses


class Home(forms.Form):
    Name = forms.CharField(max_length=30)


class StudentForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Travel_fare = forms.IntegerField()
    Eatables = forms.IntegerField()
    Sports = forms.IntegerField()
    Accessories = forms.IntegerField()
    
