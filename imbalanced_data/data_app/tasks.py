from __future__ import absolute_import

#from imbalanced_data.celery import app
#
from celery import shared_task
from data_app.models import TestOutput, Classifier, Dataset, Analysis
import random
from django.conf import settings
import sys

# Algorithm Imports
import pandas as pd
import numpy as np

from django.core.files.base import ContentFile
from StringIO import StringIO
from collections import Counter

from sklearn.cross_validation import train_test_split

# Import Classifiers
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier

# Metrics
from sklearn.metrics import classification_report
from sklearn import metrics
import matplotlib.pyplot as plt
import time

@shared_task
def test_output_creation():
  number = random.randint(0, 2000)
  test_task = TestOutput(content= "Lorem ipsum testing, whatever. " + str(number))
  test_task.save()

  return "Test Output Creation executed with number: " + str(number)

def classifier_execution(analysis, DF, classifier):

  col_length = len(DF.columns)-1

  print "Size is: %s" % str(col_length)
  print Counter(DF.iloc[:,col_length])
  print len(np.unique(DF.iloc[:,col_length]))
  pos_label = analysis.dataset.pos_label

  # Column cleaning.
  if analysis.dataset.ignore_first:
    X = np.asarray(DF.iloc[:,1:col_length])
  else:
    X = np.asarray(DF.iloc[:,0:col_length])

  Y = np.asarray(DF.iloc[:,col_length])

  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

  print X_train.shape
  print X_test.shape

  print "Executing the classifier now"

  if classifier.name == "SVM":
    print "Executing SVM"
    #clf = SVC(kernel="linear", probability=True)
    clf = DecisionTreeClassifier()
  elif classifier.name =="DT":
    print "Executing Decision Tree"
    clf = DecisionTreeClassifier()
  elif classifier.name == "kNN":
    print "Executing kNN"
    clf = KNeighborsClassifier()
  elif classifier.name == "NB":
    print "Executing Naive Bayes"
    clf = GaussianNB()
  elif classifier.name == "RF":
    print "Executing Random Forest"
    clf = RandomForestClassifier()
  elif classifier.name == "SGD":
    print "Executing Stochastic Gradient Descent"
    clf = GradientBoostingClassifier()
  elif classifier.name == "GB":
    print "Executing Gradient Boosting"
    clf = GradientBoostingClassifier()
  elif classifier.name == "Bagging":
    print "Executing Bagging"
    clf = BaggingClassifier()

  print "Fitting the data!"

  clf = clf.fit(X_train, Y_train)

  Y_pred = clf.predict(X_test)
  Y_probs = clf.predict_proba(X_test)

  print Counter(Y_pred)
  class_balance = Counter(Y_pred)

  #print "%s, %s" % class_balance[0], class_balance[1]

  output_report = classification_report(Y_test, Y_pred)
  print output_report

  fpr, tpr, thresholds = metrics.roc_curve(Y_test, Y_probs[:,1], pos_label=pos_label)
  precision, recall, thresholds = metrics.precision_recall_curve(Y_test, Y_probs[:,1], pos_label = pos_label)

  # Precision Graph
  plt.plot(recall, precision)
  pf = StringIO()
  plt.title("Precision Graph")
  plt.savefig(pf)
  precision_content_file = ContentFile(pf.getvalue())
  plt.clf()



  # ROC Curve
  plt.plot(fpr,tpr)
  plt.title("ROC Curve")
  f = StringIO()
  plt.savefig(f)
  roc_content_file = ContentFile(f.getvalue())
  plt.clf()


  # Get Various Metrics
  #roc_auc = metrics.roc_auc_score(Y_test, Y_pred)
  f1_score = metrics.f1_score(Y_test, Y_pred, pos_label=pos_label)
  precision_score = metrics.precision_score(Y_test, Y_pred, pos_label=pos_label)
  #average_precision = metrics.average_precision_score(Y_test, Y_pred, pos_label=4)
  accuracy_score = metrics.accuracy_score(Y_test, Y_pred)
  recall_score = metrics.recall_score(Y_test, Y_pred, pos_label=pos_label)

  output_object = TestOutput(content=output_report,accuracy_score=accuracy_score, precision_score=precision_score, recall_score=recall_score,f1_score=f1_score, analysis=analysis, classifier=classifier)

  roc_image_file = "roc" + str(int(time.time())) + ".png"
  precision_image_file = "prec" + str(int(time.time())) + ".png"

  output_object.precision_graph.save(precision_image_file, precision_content_file)
  output_object.roc_graph.save(roc_image_file, roc_content_file)
  output_object.save()

  analysis.completed = True
  print f1_score, precision_score, accuracy_score, recall_score
  print "Analysis done!"

  pass

@shared_task
def execute_algorithm(analysis_id):
  result = "Analysis Executed with the following id: %s" % analysis_id
  print result

  analysis = Analysis.objects.get(pk=analysis_id)
  dataset = analysis.dataset
  classifiers = analysis.classifiers.all()

  print analysis
  print analysis.description, analysis.classifiers.all(), analysis.dataset.data_file.url

  if dataset.has_header:
    print "File has header."
    header=0
  else:
    print "File doesn't have header."
    header=None

  DF = pd.read_csv(dataset.data_file.url[1:], header=header, na_values="NA")

  for key, value in enumerate(DF.dtypes):
    print key, value
    if value == 'object':
      print "Found an object"
      DF = DF.drop(DF.columns[key], axis=1)

  # Do not use identifiers in the classification.
  if analysis.ignore_first:
    DF = DF.drop(DF.columns[0])

  print DF.dtypes
  print DF.columns


  for classifier in classifiers:
    print "Executing Classifier!"
    classifier_execution(analysis, DF, classifier)

@shared_task
def test_algorithm(classifier_id, dataset_id):
  #if(classifier_name == "SVM"):
  root_media_url = settings.MEDIA_URL
  classifier = Classifier.objects.get(pk=classifier_id)
  dataset = Dataset.objects.get(pk=dataset_id)

  DF = pd.read_csv(dataset.data_file.url[1:], header=None, na_values="NA")
  DF = DF.drop(DF.columns[6], axis=1)

  print DF.dtypes

  from collections import Counter
  print Counter(DF.iloc[:,9])
  print len(np.unique(DF.iloc[:,9])) # make sure this is 2 for sane inputs

  if dataset.ignore_first:
    X = np.asarray(DF.iloc[:,1:9])
  else:
    X = np.asarray(DF.iloc[:,0:9])

  Y = np.asarray(DF.iloc[:,9])
  from sklearn.cross_validation import train_test_split
  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
  print X_train.shape
  print X_test.shape

  #import all classifiers needed here
  from sklearn.tree import DecisionTreeClassifier
  from sklearn.svm import SVC
  from sklearn.naive_bayes import GaussianNB
  from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, BaggingClassifier
  from sklearn.neighbors import KNeighborsClassifier
  from sklearn.linear_model import SGDClassifier

  #specify classifier here

  #clf = DecisionTreeClassifier()
  #clf = GaussianNB()

  clf = RandomForestClassifier()

  #clf = SVC(kernel = "linear", probability=True)
  clf = clf.fit(X_train, Y_train)

  Y_pred = clf.predict(X_test)
  Y_probs = clf.predict_proba(X_test)
  print Counter(Y_pred) #shows class imbalance

  from sklearn.metrics import classification_report
  print classification_report(Y_test, Y_pred)
  output_report = classification_report(Y_test, Y_pred)

  from sklearn import metrics
  import matplotlib.pyplot as plt
  import time

  fpr, tpr, thresholds = metrics.roc_curve(Y_test, Y_probs[:,1], pos_label=4)

  precision, recall, thresholds = metrics.precision_recall_curve(Y_test, Y_probs[:,1], pos_label = 4)

  # Precision Graph
  plt.plot(recall, precision)
  pf = StringIO()
  plt.title("Precision Graph")
  plt.savefig(pf)
  precision_content_file = ContentFile(pf.getvalue())
  plt.clf()

  # ROC Curve
  plt.plot(fpr,tpr)
  plt.title("ROC Curve")
  f = StringIO()
  plt.savefig(f)
  roc_content_file = ContentFile(f.getvalue())
  plt.clf()

  # Get Various Metrics
  #roc_auc = metrics.roc_auc_score(Y_test, Y_pred)
  f1_score = metrics.f1_score(Y_test, Y_pred, pos_label=4)
  precision_score = metrics.precision_score(Y_test, Y_pred, pos_label=4)
  #average_precision = metrics.average_precision_score(Y_test, Y_pred, pos_label=4)
  accuracy_score = metrics.accuracy_score(Y_test, Y_pred)
  recall_score = metrics.recall_score(Y_test, Y_pred, pos_label=4)

  output_object = TestOutput(content=Counter(Y_pred), accuracy_score=accuracy_score, precision_score=precision_score, recall_score=recall_score,f1_score=f1_score)

  roc_image_file = "roc" + str(int(time.time())) + ".png"
  precision_image_file = "prec" + str(int(time.time())) + ".png"

  output_object.precision_graph.save(precision_image_file, precision_content_file)
  output_object.roc_graph.save(roc_image_file, roc_content_file)
  output_object.save()


  print f1_score, precision_score, accuracy_score, recall_score
  print "Analysis done!"