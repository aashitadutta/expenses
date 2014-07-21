from django.db import models

# Create your models here.
class WeeklyExpenses(models.Model):
    Name = models.CharField(max_length=30,default = "Null")
    Travel_fare = models.IntegerField(default=10)
    Eatables = models.IntegerField(default=5)
    Sports = models.IntegerField(default=5)
    Accessories = models.IntegerField(default=5)

    
    def __unicode__(self):
        return str(self.Name)
