from django.contrib import admin
from data_app.models import Dataset, Classifier, TestOutput
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
  pass

admin.site.register(Dataset, MyModelAdmin)
admin.site.register(Classifier)
admin.site.register(TestOutput)