from .models import UserData
from .serializers import SerializerData
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle

class StudentModelViewSet(viewsets.ModelViewSet):
  queryset = UserData.objects.all()
  serializer_class = SerializerData
  authentication_classes=[TokenAuthentication]
  permission_classes=[IsAuthenticated]
  throttle_classes = [UserRateThrottle]

  