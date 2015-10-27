from django.contrib import admin
from .models import Post, Comment

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm



admin.site.register(Post)
admin.site.register(Comment)
