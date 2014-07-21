from django.shortcuts import render

from student.models import *

from student.forms import StudentForm

from django.http import HttpResponseRedirect

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
               obj = WeeklyExpenses(Name=Name,Travel_Fare=Travel_Fare, Eatables=Eatables,Sports=Sports,Accessories=Accessories)
               Total = obj.Travel_fare+obj.Eatables+obj.Sports+obj.Accessories
               obj.save()
               return HttpResponseRedirect('student/stud/')
               return render(request, 'student/exp.html', {'Total':total})  

           else:
                 form = StudentForm()
                 return render(request,'student/contact_form.html', {'form':form})
   
    else:  
          form = StudentForm()
          return render(request, 'student/contact_form.html', {'form':form})  
     
              
