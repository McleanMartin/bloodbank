from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from core.serializers import *
from core.models import *
from core.forms import *


def index(request):
    return render(request,'rest_framework/index-api.html')

class RegisterApiView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self,request,format=None): 
        serializer = self.serializer_class(data=request.data)
        response_data = {}
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            response_data['user'] = serializer.data
            response_data['access'] = str(token)
            response_data['status'] = 'success'
            return Response(response_data,)
        return Response(serializer.errors,)

class Fetch_Location(APIView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["facilites"] = Location.objects.all()
        return Response(context)

class Fetch_User_Profile(APIView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Donor_Card.objects.get(user=user)
        return Response(context)

class Fetch_Alerts(APIView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["alerts"] = Alerts.objects.all()
        return Response(context)
    
    
    
    

