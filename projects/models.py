from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    VISIBILITY_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
        ('shared', 'Shared')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Link(models.Model):
    url = models.URLField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    # The project field in the Link model represents the project to which the link belongs.
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='links')

    def __str__(self):
        return self.url
    

class Team(models.Model):
    members = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams', blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='teams', blank=True)


    def __str__(self):
        return f'Team {self.id}'
