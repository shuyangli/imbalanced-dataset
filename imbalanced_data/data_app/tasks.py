from __future__ import absolute_import

#from imbalanced_data.celery import app
#
from celery import shared_task
from data_app.models import TestOutput
from data_app import utils
import random
from django.conf import settings
import sys

# Algorithm Imports
import pandas as pd
import numpy as np

from django.core.files import ContentFile
@shared_task
def test(param):
  return 'The test task executed  with argument "%s" ' % param

@shared_task
def test_output_creation():
  number = random.randint(0, 2000)
  test_task = TestOutput(content= "Lorem ipsum testing, whatever. " + str(number))
  test_task.save()

  return "Test Output Creation executed with number: " + str(number)

@shared_task
def test_algorithm(classifier_name, file_name):
  #if(classifier_name == "SVM"):
  root_media_url = settings.MEDIA_URL
  print 'GETTING SETTINGS"'
  print root_media_url
  print file_name

  file_url = root_media_url + file_name
  print file_url
  DF = pd.read_csv(file_name, header=None, na_values="NA")
  DF = DF.drop(DF.columns[6], axis=1)
  print DF.dtypes

  from collections import Counter
  print Counter(DF.iloc[:,9])
  print len(np.unique(DF.iloc[:,9])) # make sure this is 2 for sane inputs

  X = np.asarray(DF.iloc[:,1:9])
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
  #clf = RandomForestClassifier()
  clf = SVC(kernel = "linear", probability=True)
  clf = clf.fit(X_train, Y_train)

  Y_pred = clf.predict(X_test)
  Y_probs = clf.predict_proba(X_test)
  Counter(Y_pred) #shows class imbalance
  from sklearn.metrics import classification_report
  print classification_report(Y_test, Y_pred)
  from sklearn import metrics
  fpr, tpr, thresholds = metrics.roc_curve(Y_test, Y_probs[:,1], pos_label=4)
  import matplotlib.pyplot as plt
  plt.plot(fpr,tpr)
  plt.show()

  #Precision Recall curve
  from sklearn.metrics import precision_recall_curve
  precision, recall, thresholds = precision_recall_curve(Y_test, Y_probs[:,1], pos_label = 4)

  plt.plot(recall, precision)
  plt.show()



@shared_task
def run_naive_bayes():
  pass

@shared_task
def run_svm():
  pass

@shared_task
def run_decision_tree():
  pass

@shared_task
def run_random_forest():
  pass

@shared_task
def run_k_nearest():
  pass

@shared_task
def run_stochastic():
  pass

@shared_task
def run_gradient():
  pass

@shared_task
def run_bagging():
  pass