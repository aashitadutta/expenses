from django.contrib import admin

# Register your models here.
from student.models import WeeklyExpenses

class WeeklyExpensesAdmin(admin.ModelAdmin):
    fields = ['Travel_fare', 'Eatables', 'Sports',
              'Accessories', 'Total']

admin.site.register(WeeklyExpenses, WeeklyExpensesAdmin)
