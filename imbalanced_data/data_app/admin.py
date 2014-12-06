from django.contrib import admin
from data_app.models import Dataset, Classifier
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
  pass

admin.site.register(Dataset, MyModelAdmin)
admin.site.register(Classifier)
