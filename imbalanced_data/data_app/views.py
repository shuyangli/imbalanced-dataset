from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, DatasetSerializer, ClassifierSerializer, TestOutputSerializer
from django.contrib.auth.models import User, Group
from data_app.models import *
from django.views.decorators.csrf import csrf_exempt
import random

# Create your views here.
# @csrf_exempt
# class UserViewSet(viewsets.ModelViewSet):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer

# @csrf_exempt
# class GroupViewSet(viewsets.ModelViewSet):
#   queryset = Group.objects.all()
#   serializer_class = GroupSerializer

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

class ClassifierViewSet(viewsets.ModelViewSet):
  queryset = Classifier.objects.all()
  serializer_class = ClassifierSerializer

@api_view(['GET', 'POST'])
def output_list(request):
  if request.method == 'GET':
    test_outputs = TestOutput.objects.all()
    serializer = TestOutputSerializer(test_outputs, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = TestOutputSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@csrf_exempt
def user_list(request):
  if request.method == 'GET':
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@csrf_exempt
def group_list(request):
  if request.method == 'GET':
    groups = Group.objects.all()
    serializer =  GroupSerializer(groups, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
