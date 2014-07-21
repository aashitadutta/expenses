from django.db import models

# Create your models here.
class WeeklyExpenses(models.Model):
    Name = models.CharField(max_length=30,default = "Null")
    Travel_fare = models.IntegerField(default=10)
    Eatables = models.IntegerField(max_length=10)
    Sports = models.IntegerField(max_length=10)
    Accessories = models.IntegerField(max_length=10)
    Total = models.IntegerField(max_length=10)
    
    def __unicode__(self):
        return str(self.Name)
