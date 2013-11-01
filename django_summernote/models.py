from django.db import models
from django.core.files.storage import default_storage
from django_summernote.settings import summernote_config


__all__ = ['Attachment', ]


def _get_attachment_storage(self):
    if summernote_config['attachment_storage']:
        return summernote_config['attachment_storage']()
    else:
        return default_storage


class Attachment(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to=summernote_config['attachment_upload_to'],
                            storage=_get_attachment_storage())

    uploaded = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
