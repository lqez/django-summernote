from django.shortcuts import render
from django.utils import simplejson
from django_summernote.settings import summernote_config


def editor(request, id):
    return render(request, 'django_summernote/editor.html', {
        'id': id,
        'toolbar': simplejson.dumps(summernote_config['toolbar']),
    })
