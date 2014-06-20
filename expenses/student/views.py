from django.shortcuts import render

from student.models import WeeklyExpenses

from student.forms import StudentForm

def stud(request):
    if request.method=='POST':
	   form = StudentForm(request.POST)
           if forms.is_valid():
               cd = form.cleaned_data['name']
               obj = WeeklyExpenses.objects.values('name', 'Travel_Fare', 'Eatables', 'Sports', 'Accessories', 'Total')
               return render(request, 'exp.html', {'obj':obj})
    else:
           form = StudentForm()
         
        #Total = obj.Travel_Fare+obj.Eatables+obj.Sports
#+obj.Accessories
    return render(request, 'contact_form.html', {'form':form})
    

  #Travel_Fare:e.Travel_Fare
   #Eatables:e.Eatables
   #Sports:e.Sports
   #Accessories:e.Accessories

 
