#from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from data_app.models import *
from django.views.decorators.csrf import csrf_exempt


class TestOutputSerializer(serializers.ModelSerializer):
  class Meta:
    model = TestOutput
    fields = ('id', 'content')

class UserSerializer(serializers.ModelSerializer):
  username = serializers.CharField()
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'groups')

class GroupSerializer(serializers.ModelSerializer):
  name = serializers.CharField()
  class Meta:
    model = Group
    fields = ('id', 'name')

class DatasetSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Dataset
    fields = ('id', 'url', 'name', 'description', 'data_file')

class ClassifierSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Classifier
    fields = ('id', 'url', 'name', 'description', 'program_file')