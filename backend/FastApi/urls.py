from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token,ObtainAuthToken
from core.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='api-index'),
    path('api/register',RegisterApiView.as_view(),name="register"),
    path('api/login',obtain_auth_token,name="login"),
    path('api/locations',Fetch_Location.as_view(),name="location"),
    path('api/profile',Fetch_User_Profile.as_view(),name="profile"),
    path('api/alerts',Fetch_Alerts.as_view(),name="alerts"),
    
]

