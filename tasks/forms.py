from turtle import title
from django import forms
from .models import *
from .views import *
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    tittle = forms.CharField(widget=forms.TimeInput(attrs={'placeholder': 'Add a new task.'}))


    class Meta:
        model = Task
        fields = '__all__'