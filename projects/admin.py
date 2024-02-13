from django.contrib import admin

# Register your models here.
from .models import Link, Project
admin.site.register(Project)
admin.site.register(Link)