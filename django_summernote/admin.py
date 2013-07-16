from django.contrib import admin
from django.db import models
from django_summernote.widgets import SummernoteWidget


class SummernoteModelAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': SummernoteWidget}}
