from django.db import models

# Create your models here.
class Dataset(models.Model):
  data_file = FileField()