from django.db import models


Task_choice = [
    ('Inprogress','Inprogress'),
    ('Completed','Completed'),
    ('Cancelled','Cancelled'),
    ('Pending','Pending'),
]



class Task(models.Model):
    name = models.CharField(max_length=20,unique =True )
    description = models.TextField()
    task_status = models.CharField(max_length=25,choices=Task_choice,default='Pending')
    task_deadline = models.DateTimeField()
    task_created_date = models.DateTimeField(auto_now_add = True)
    task_completed_date = models.DateTimeField(auto_now_add = True)
    
