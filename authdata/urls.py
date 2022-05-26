from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('api/messages', views.StudentModelViewSet, basename='api/messages')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('gettoken/', obtain_auth_token)

]
