from django.shortcuts import render
from student.models import *
from student.forms import Home, StudentForm
from django.http import HttpResponse

def home(request):
	if request.method=='POST':
		return HttpResponseRedirect('/home/')
	return render(request,'login.html')

def login(request):
        if request.method=='POST':
 		form = Home(request.POST)
 		if form.is_valid():
 			cd = form.cleaned_data
 			Name = cd['Name'] 
 			new = WeeklyExpenses(Name=Name)
 			new.save()
 			return HttpResponseRedirect('/login/')
 	else:
 		form = Home()		
 	return render(request,'boom.html',{'form':form})

def stud(request):
    if request.method=='POST':
	   form = StudentForm(request.POST)
           if form.is_valid():               
               cd = form.cleaned_data
	       Name = cd ['Name']
               Travel_fare = cd ['Travel_fare']
               Eatables = cd ['Eatables'] 
               Sports = cd ['Sports']
               Accessories = cd ['Accessories']
               obj = WeeklyExpenses(Name=Name,Travel_fare=Travel_fare, Eatables=Eatables,Sports=Sports,Accessories=Accessories)
               obj.save()
               expenses = WeeklyExpenses.objects.values('Travel_fare', 'Eatables', 'Sports','Accessories') 
               #i = WeeklyExpenses.objects.get(pk='client_id')
               Travel_fare = obj.Travel_fare
               Eatables = obj.Eatables
               Sports = obj.Sports
               Accessories = obj.Accessories
               Total = obj.Travel_fare + obj.Eatables + obj.Sports + obj.Accessories
               return render(request, 'student/result.html',{'Total':Total,'expenses':expenses, 'Travel_fare':Travel_fare,'Eatables':Eatables,'Sports':Sports,'Accessories':Accessories})
    else:
        form = StudentForm() 
    return render(request, 'student/contact_form.html', {
        'form': form
    })


