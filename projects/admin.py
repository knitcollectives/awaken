from django.contrib import admin
from django.db import models
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["title", "published"]}),
        ("Description", {'field', ["description"]}),
        ("Image File", {'field', ["image"]}),
    ]

admin.site.register(Project, ProjectAdmin)
