from django.contrib import admin
from .models import Blogpost, Repository
# Register your models here.

admin.site.register(Blogpost)
admin.site.register(Repository)