from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','description','task_status','task_deadline']

        widgets ={
            'task_deadline' : forms.DateTimeInput(attrs={'type':'date','class':'form-control'}),
            
        }

class TaskCompleteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','description','task_status','task_deadline']

        widgets ={
            'name' : forms.TextInput(attrs={'readonly':'true'}),
            'description' : forms.Textarea(attrs={'readonly' : 'true'})
            
        }

