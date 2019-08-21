from django.db import models
from datetime import datetime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20)
    published = models.DateTimeField("date published", default=datetime.now())
    image = models.FilePathField(path="projects/static/img")


    def __str__(self):
        return self.title
