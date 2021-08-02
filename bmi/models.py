from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userdata(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.weight}/{self.height}"


    def save(self, *args, **kwargs):
        self.bmi = self.weight / (self.height * self.height)
        super().save(*args, **kwargs)
        
    
    @property
    def bmi_category(self):
        if self.bmi < 18  :
            return "Underweight"
        elif self.bmi > 18.5 and self.bmi <24.9 :
            return "Normal" 
        elif self.bmi >25 and self.bmi <29.9:
            return "Overwieight"
        else:
            return "Obese"
        
    @property
    def bmi_color(self):
        if self.bmi < 18  :
            return "Orange"
        elif self.bmi > 18.5 and self.bmi <24.9 :
            return "Green" 
        elif self.bmi >25 and self.bmi <29.9:
            return "Blue"
        else:
            return "Red"
    
class Suggestion(models.Model):
    category_choices = (
        ("Underweight","Underweight"),
        ("Normal","Normal"),
        ("Overweight","Overweight"),
        ("Obese","Obese"),
    )
    category = models.CharField(max_length=25, choices=category_choices)
    message = models.TextField()