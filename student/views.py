from django.shortcuts import render

from student.models import WeeklyExpenses

from student.forms import StudentForm
from django.http import HttpResponseRedirect

def stud(request):
    if request.method=='POST':
	   form = StudentForm(request.POST)
           if form.is_valid():
               cd = form.cleaned_data['Name']
               obj = WeeklyExpenses(Name=Name)
               obj.save()
               return HttpResponseRedirect('/student/stud/')
    else:
           form = StudentForm()
           return render(request, 'student/contact_form.html', {'form':form})
 

def display(request):
    obj = WeeklyExpenses.objects.get(id=1)
    Name = obj.Name   
    Travel_Fare = obj.Travel_Fare
    Eatables = obj.Eatables
    Sports = obj.Sports
    Accessories = obj.Accessories
    Total = obj.Travel_Fare+obj.Eatables+obj.Sports
    +obj.Accessories
    return render(request, 'exp.html', {'Travel_Fare': Travel_Fare, Eatables:'Eatables', 'Sports':Sports, 'Accessories': Accessories })
