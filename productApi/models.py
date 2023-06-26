from djongo import models
from django import forms
# from djangotoolbox.fields import ListField
import datetime

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

class Product(models.Model):
    name = models.CharField(max_length=100)
    ownerName = models.CharField(max_length=100)
    masterName = models.CharField(max_length=100)
    startDate = models.DateField()
    developers = models.ArrayField(
        model_container=Developer,
    )
    methodology = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
