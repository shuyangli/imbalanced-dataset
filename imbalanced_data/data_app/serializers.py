#from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from data_app.models import *
from django.views.decorators.csrf import csrf_exempt

class CustomFileField(serializers.FileField):
  def to_native(self, value):
    request = self.context.get('request', None)
    return request.build_absolute_uri(value.url)

class AnalysisSerializer(serializers.ModelSerializer):
  test_outputs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  class Meta:
    model = Analysis
    fields = ('id', 'title', 'description', 'dataset', 'classifiers', 'created', 'modified', 'completed', 'has_header', 'pos_label', 'ignore_first', 'test_outputs')

class TestOutputSerializer(serializers.ModelSerializer):
  class Meta:
    model = TestOutput
    fields = ('id', 'content', 'precision_graph', 'roc_graph', 'created', 'accuracy_score', 'precision_score', 'recall_score', 'f1_score', 'classifier', 'analysis')

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

class DatasetSerializer(serializers.ModelSerializer):
  #data_file = serializers.FileField()
  name = serializers.CharField()
  description =  serializers.CharField()
  #data_file = serializers.FileField(use_url=False)
  data_file = CustomFileField()
  class Meta:
    model = Dataset
    fields = ('id', 'name', 'description', 'data_file')

class ClassifierSerializer(serializers.ModelSerializer):
  class Meta:
    model = Classifier
    fields = ('id', 'name', 'description')