from django.db import models
from django.db.models.signals import post_save

class Classifier(models.Model):
  """
    Params:

    name - Name of the given classifier.
    description - Description of the Classifier. Are we running Apriori, FP-Growth, etc.
    program_file - Most likely the external script that will actually be used to execute said classifier.
  """

  name = models.CharField(max_length=255, blank=True)
  description = models.TextField(blank=True)

  def __unicode__(self):
    return self.name

class TestOutput(models.Model):
  content = models.TextField()
  precision_graph = models.ImageField(upload_to="outputs", blank=True, default='')
  roc_graph = models.ImageField(upload_to="outputs", blank=True, default='')
  accuracy_score = models.FloatField(blank=True, default=0)
  precision_score = models.FloatField(blank=True, default=0)
  recall_score = models.FloatField(blank=True, default=0)
  f1_score = models.FloatField(blank=True, default=0)
  #roc_auc = models.FloatField(blank=True, default=0)
  average_precision = models.FloatField(blank=True, default=0)
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  analysis = models.ForeignKey("Analysis", blank=True, related_name = "test_outputs")

  def __unicode__(self):
    return "Test Output: " % self.id

class Dataset(models.Model):
  """
  Params:
  name: A name or title of the dataset, for easy recognition by the end user.
  description: A description of the contents of the dataset.
  data_file: The actual dataset file, uploaded by the user.

  Potentially Add: ForeignKey reference to User, so that the respective files can be associated with a given user?
  """

  name = models.CharField(max_length=255, blank=True)
  description = models.TextField(blank=True)
  data_file = models.FileField(upload_to="datasets")
  pos_label = models.IntegerField(default=4, blank=True)
  has_header = models.BooleanField(default=False)
  ignore_first = models.BooleanField(default=True)

  def __unicode__(self):
    return self.name

class Analysis(models.Model):
  """
    Model that is created whenever the user wants to run an analysis on an imbalanced dataset. Should most likely have a ForeignKey corresponding to the user that created it, in addition to a timestamp corresponding to when it was created, it's status of if it is completed or not, etc.

    Should it run only one classifier at a time or should the user be able to select the classifiers that they would want to run with this specific dataset?

    Params:
    title: A title for the simulation run for easy understanding of what was occurring.
    description: A description of the simulation so other users can know what was run within it.
  """

  title = models.CharField(max_length=255, blank=True, default='')
  description = models.TextField(blank=True, default='')
  classifiers = models.ManyToManyField(Classifier, blank=True)
  dataset = models.ForeignKey(Dataset, blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  completed = models.BooleanField(default=False)
  has_header = models.BooleanField(default=False)
  ignore_first = models.BooleanField(default=False)
  pos_label = models.IntegerField(default=1)

  def __unicode__(self):
    if self.title:
      return self.title
    else:
      return "Analysis: %s"  % self.id

# Import utils for post_save tasks.
from utils import create_analysis_task

# After Creation For Creating Tasks
post_save.connect(create_analysis_task, sender=Analysis, dispatch_uid="create_new_analysis")


