#from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from data_app.models import Dataset


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ('url', 'name')

class DatasetSerializer(serializers.HyperlinkedModelSerializer):
  #pk = serializers.IntegerField(read_only=True)
  #title = serializers.CharField()
  #description = serializers.TextField()

  class Meta:
    model = Dataset
