from django.contrib import admin

# Register your models here.
from api import models

admin.site.register(models.Employee)
admin.site.register(models.Student)
