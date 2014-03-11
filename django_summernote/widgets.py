import json
import os
from django import forms
from django.core.urlresolvers import reverse_lazy
from django.template import Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from django_summernote.settings import summernote_config
from django.conf import settings

__all__ = ['SummernoteWidget', 'SummernoteInplaceWidget']


def _static_url(url):
    return os.path.join(settings.STATIC_URL, url)


class SummernoteWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        attrs_for_textarea = attrs.copy()
        attrs_for_textarea['hidden'] = 'true'
        html = super(SummernoteWidget, self).render(name,
                                                    value,
                                                    attrs_for_textarea)

        final_attrs = self.build_attrs(attrs)
        del final_attrs['id']  # Use original attributes without id.

        url = reverse_lazy('django_summernote-editor',
                           kwargs={'id': attrs['id']})
        html += render_to_string('django_summernote/widget_iframe.html',
                                 {
                                     'id': '%s-iframe' % (attrs['id']),
                                     'src': url,
                                     'attrs': flatatt(final_attrs),
                                     'width': summernote_config['width'],
                                     'height': summernote_config['height'],
                                 })
        return mark_safe(html)


class SummernoteInplaceWidget(forms.Textarea):
    class Media:
        css = {'all': (
            '//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap.no-icons.min.css',
            '//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.min.css',
            _static_url('django_summernote/summernote.css'),
        )}
        js = (
            '//code.jquery.com/jquery-1.9.1.min.js',
            '//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js',
            _static_url('django_summernote/summernote.min.js'),
            _static_url('django_summernote/jquery.ui.widget.js'),
            _static_url('django_summernote/jquery.iframe-transport.js'),
            _static_url('django_summernote/jquery.fileupload.js'),
        )
        if summernote_config['lang'] != 'en-US':
            js += (_static_url(
                'django_summernote/lang/summernote-%s.js' % (summernote_config['lang'])
            ), )

    def render(self, name, value, attrs=None):
        attrs_for_textarea = attrs.copy()
        html = super(SummernoteInplaceWidget, self).render(name,
                                                           value,
                                                           attrs_for_textarea)

        html += render_to_string(
            'django_summernote/widget_inplace.html',
            Context(
                {
                    'id': attrs['id'],
                    'toolbar': json.dumps(summernote_config['toolbar']),
                    'lang': summernote_config['lang'],
                    'height': summernote_config['height'],
                    'url': {
                        'upload_attachment':
                        reverse_lazy('django_summernote-upload_attachment'),
                    },
                }
            )
        )
        return mark_safe(html)
