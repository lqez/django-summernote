from django.conf import settings
from django.shortcuts import render
from django.utils import simplejson


def editor(request, id):
    config = getattr(settings, 'SUMMERNOTE_CONFIG', {
        'toolbar': [
            ['style', ['style']],
            ['fontsize', ['fontsize']],
            ['color', ['color']],
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['para', ['ul', 'ol', 'height']],
            ['insert', ['link', 'picture']],
            ['help', ['help']],
        ],
    })
    return render(request, 'django_summernote/editor.html', {
        'id': id,
        'toolbar': simplejson.dumps(config['toolbar']),
    })
