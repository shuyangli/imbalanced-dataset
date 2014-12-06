from __future__ import absolute_import

#from imbalanced_data.celery import app
#
from celery import shared_task
from data_app.models import TestOutput
import random

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