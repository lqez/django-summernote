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
    'iframe': True,
    'airMode': False,
    'empty': ('<p><br/></p>', '<p><br></p>'),

    'width': 720,
    'height': 480,
    'toolbar': [
        ['style', ['style']],
        ['font', ['bold', 'italic', 'underline', 'superscript', 'subscript',
                  'strikethrough', 'clear']],
        ['fontname', ['fontname']],
        ['fontsize', ['fontsize']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['height', ['height']],
        ['table', ['table']],
        ['insert', ['link', 'picture', 'video', 'hr']],
        ['view', ['fullscreen', 'codeview']],
        ['help', ['help']],
    ],
    'lang': 'en-US',

    'attachment_upload_to': uploaded_filepath,
    'attachment_storage_class': None,
    'attachment_filesize_limit': 1024 * 1024,

    'inplacewidget_external_css': (
        '//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap.no-icons.min.css',
        '//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.min.css',
    ),
    'inplacewidget_external_js': (
        '//code.jquery.com/jquery-1.9.1.min.js',
        '//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js',
    ),
}

summernote_config = SETTINGS_DEFAULT.copy()
summernote_config.update(SETTINGS_USER)
