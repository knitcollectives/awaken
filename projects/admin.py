from django.contrib import admin
from django.db import models
from project.models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
