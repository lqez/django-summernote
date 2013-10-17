from django.conf import settings

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
}

summernote_config = dict(SETTINGS_DEFAULT.items() + SETTINGS_USER.items())
