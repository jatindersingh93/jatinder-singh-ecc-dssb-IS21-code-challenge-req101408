from djongo import models
from django import forms
# from djangotoolbox.fields import ListField
import datetime

# relationship model to capture Developer names
class Developer(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = (
            'name',
        )
# Product model to handel all product keys
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500)
    ownerName = models.CharField(max_length=500)
    masterName = models.CharField(max_length=500)
    startDate = models.DateField()
    developers = models.ArrayField(
        model_container=Developer,
    )
    methodology = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
