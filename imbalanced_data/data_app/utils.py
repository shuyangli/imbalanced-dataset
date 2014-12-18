from data_app.models import Analysis
from data_app.tasks import execute_algorithm
import pandas as pd

def create_analysis_task(sender, instance, **kwargs):
  print "Create Analysis Task called!"

  # Create a new algorithm execution task.
  # Pass in the Analysis Task's ID to Celery for processing purposes.
  print instance.id
  print instance.classifiers.all()
  print instance.dataset

  execute_algorithm(instance.id)

# Create a task signal that executes on a Many to Many changed relationship?

def run_svm(datasets, classifiers):
  pass
