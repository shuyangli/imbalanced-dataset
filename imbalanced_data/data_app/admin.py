from django.contrib import admin
from data_app.models import Dataset, Classifier, TestOutput, Analysis
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
  pass

class TestOutputInline(admin.StackedInline):
  model = TestOutput

class AnalysisAdmin(admin.ModelAdmin):
  inlines = [
    TestOutputInline
  ]
admin.site.register(Dataset, MyModelAdmin)
admin.site.register(Classifier)
admin.site.register(TestOutput)
admin.site.register(Analysis, AnalysisAdmin)