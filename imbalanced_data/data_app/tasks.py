from __future__ import absolute_import

from imbalanced_data.celery import app

@app.task
def run_naive_bayes():
  pass

@app.task
def run_svm():
  pass

@app.task
def run_decision_tree():
  pass

@app.task
def run_random_forest():
  pass

@app.task
def run_k_nearest():
  pass

@app.task
def run_stochastic():
  pass

@app.task
def run_gradient():
  pass

@app.task
def run_bagging:
  pass