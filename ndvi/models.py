from django.db import models

# Create your models here.
from django.db import models

class Ndvi(models.Model):
    title = models.CharField(max_length=200)
    polygon = models.TextField()
    ndvi = models.FloatField(default=0.0)
    cvs_data = models.TextField(default="")
    start_date = models.TextField()
    end_date = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title