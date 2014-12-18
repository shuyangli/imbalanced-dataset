from django.shortcuts import render
from django.http import Http404

from rest_framework import viewsets, generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, GroupSerializer, DatasetSerializer, ClassifierSerializer, TestOutputSerializer, AnalysisSerializer
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

  resource_name = 'analyses'

  def get(self, request, format=None):
    analyses = Analysis.objects.all()
    serializer = AnalysisSerializer(analyses, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    print "POST REQUEST CALLED"
    print request
    print request.data
    form_data = request.data
    serializer = AnalysisSerializer(data=form_data)
    print form_data['dataset']
    response = "POST works!"
    dataset_file = Dataset.objects.get(pk=form_data['dataset'])
    classifier = Classifier.objects.get(pk=form_data['classifier_ids'][0])

    classifier_id = form_data['classifier_ids'][0]
    dataset_id = form_data['dataset']
    print form_data
    print "GOT HERE"
    print classifier.name
    print dataset_file.data_file.url
    #test_algorithm.delay(classifier_id, dataset_id)

    #"files/datasets/breast-cancer_EKTk2SE.csv")

    if serializer.is_valid():
      print "VALID FORM!"
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnalysisDetail(APIView):
  def get_object(self, pk):
    try:
      return Analysis.objects.get(pk=pk)
    except Analysis.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    analysis  = self.get_object(pk)
    serializer = AnalysisSerializer(analysis)
    return Response(serializer.data)

class TestOutputList(APIView):
  """
  List all output or create a new one
  """

  resource_name = 'test-output'

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

  resource_name = 'users'

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

  resource_name = 'classifiers'

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

  resource_name = 'dataset'

  def get(self, request, format=None):
    datasets = Dataset.objects.all()
    serializer = DatasetSerializer(datasets, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = DatasetSerializer(data=request.data)
    print request.data
    print request.FILES
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DatasetDetail(APIView):
  def get_object(self, pk):
    try:
      return Dataset.objects.get(pk=pk)
    except Dataset.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    dataset  = self.get_object(pk)
    serializer = DatasetSerializer(dataset)
    return Response(serializer.data)

