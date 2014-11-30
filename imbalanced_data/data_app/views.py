from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, DatasetSerializer
from django.contrib.auth.models import User, Group
from data_app.models import Dataset
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer