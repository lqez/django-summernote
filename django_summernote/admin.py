from django.contrib import admin
from django.db import models
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.models import Attachment
from django_summernote.settings import summernote_config, get_attachment_model

__widget__ = SummernoteWidget if summernote_config['iframe'] \
    else SummernoteInplaceWidget


class SummernoteInlineModelAdmin(admin.options.InlineModelAdmin):
    formfield_overrides = {models.TextField: {'widget': __widget__}}


class SummernoteModelAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': __widget__}}


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', 'uploaded']
    search_fields = ['name']
    ordering = ('-id',)

admin.site.register(get_attachment_model(), AttachmentAdmin)
