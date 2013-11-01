import os
import uuid
from datetime import datetime
from django.conf import settings


def uploaded_filepath(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    today = datetime.now().strftime('%Y-%m-%d')
    return os.path.join('django-summernote', today, filename)


SETTINGS_USER = getattr(settings, 'SUMMERNOTE_CONFIG', {})
SETTINGS_DEFAULT = {
    'width': 720,
    'height': 480,
    'toolbar': [
        ['style', ['style']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['para', ['ul', 'ol', 'height']],
        ['insert', ['link', 'picture']],
        ['help', ['help']],
    ],
    'attachment_upload_to': uploaded_filepath,
    'attachment_storage': None,
    'attachment_filesize_limit': 1024 * 1024,
}

summernote_config = dict(SETTINGS_DEFAULT.items() + SETTINGS_USER.items())
