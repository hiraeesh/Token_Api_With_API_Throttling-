
import email
from venv import create
from django.db import models
from datetime import datetime   
from django.contrib.auth.models import User
# Create your models here.

class UserData(models.Model):
   
    id=models.AutoField(primary_key=True)
    message= models.CharField(max_length=2000)
    created_at= models.TimeField(default=datetime.now, blank=True)
    updated_at= models.TimeField(default=datetime.now, blank=True)
    dom_element= models.ManyToManyField(User)

   
    
    def created_by(self):
        for p in self.dom_element.all():
            id = p.id
            username=p.username
            email=p.email
        
            return id,username,email


