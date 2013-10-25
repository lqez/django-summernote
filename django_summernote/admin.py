from django.contrib import admin
from django.db import models
from django_summernote.widgets import SummernoteWidget
from django_summernote.models import Attachment


class SummernoteModelAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': SummernoteWidget}}


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', 'uploaded']
    search_fields = ['name']
    ordering = ('-id',)

admin.site.register(Attachment, AttachmentAdmin)
