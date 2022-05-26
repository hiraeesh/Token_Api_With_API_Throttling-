from django.contrib import admin
from .models import UserData
# Register your models here.

@admin.register(UserData)
class AlluserData(admin.ModelAdmin):
    list_display=['id','message','created_at','updated_at','created_by']
