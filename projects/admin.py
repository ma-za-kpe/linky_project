from django.contrib import admin

# Register your models here.
from .models import Link, Project, Team
admin.site.register(Project)
admin.site.register(Link)
admin.site.register(Team)