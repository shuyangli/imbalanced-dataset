from django.contrib import admin
from data_app.models import Dataset
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
  pass

admin.site.register(Dataset, MyModelAdmin)
