from django.db import models
from django_summernote.settings import summernote_config


class Attachment(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to=summernote_config['attachment_upload_to'],
                            storage=summernote_config['attachment_storage'])

    uploaded = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
