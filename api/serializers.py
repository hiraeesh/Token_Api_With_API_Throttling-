from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import UserData

class SerializerData(serializers.ModelSerializer):
    class Meta:
        model=UserData
        fields=['id','message','created_at','updated_at','created_by']
        