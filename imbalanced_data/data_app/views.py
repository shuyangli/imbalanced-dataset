from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, GroupSerializer, DatasetSerializer, ClassifierSerializer, TestOutputSerializer
from django.contrib.auth.models import User, Group
from data_app.models import *
from django.views.decorators.csrf import csrf_exempt

from data_app.tasks import test_algorithm
import random

# class DatasetViewSet(viewsets.ModelViewSet):
#     queryset = Dataset.objects.all()
#     serializer_class = DatasetSerializer

# class ClassifierViewSet(viewsets.ModelViewSet):
#   queryset = Classifier.objects.all()
#   serializer_class = ClassifierSerializer


class AnalysisTaskList(APIView):
  """
  Testing submission of analysis tasks.
  """

  def get(self, request, format=None):
    response = Response("GET works!", status=status.HTTP_200_OK)
    return response

  def post(self, request, format=None):
    form_data = request.data
    response = "POST works!"
    print form_data

    test_algorithm.delay("SVM", "datasets/breast-cancer_EKTk2SE.csv")
    return Response(response, status=status.HTTP_200_OK)

class TestOutputList(APIView):
  """
  List all output or create a new one
  """

  def get(self, request, format=None):
    test_outputs = TestOutput.objects.all()
    serializer = TestOutputSerializer(test_outputs, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = TestOutputSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
  """
  List all users or create a new one.
  """

  def get(self, request, format=None):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupList(APIView):
  """
  List all groups or create a new one.
  """

  def get(self, request, format=None):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassifierList(APIView):
  """
  List all classifiers or create a new one.
  """

  def get(self, request, format=None):
    classifiers = Classifier.objects.all()
    serializer = ClassifierSerializer(classifiers, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = Classifier(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DatasetList(APIView):
  """
  List all datasets or create a new one.
  """

  def get(self, request, format=None):
    datasets = Dataset.objects.all()
    serializer = DatasetSerializer(datasets, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = DatasetSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
