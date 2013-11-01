from django import forms
from django.core.urlresolvers import reverse_lazy
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from django_summernote.settings import summernote_config


class SummernoteWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        attrs_for_textarea = attrs.copy()
        attrs_for_textarea['hidden'] = 'true'
        html = super(SummernoteWidget, self).render(name,
                                                    value,
                                                    attrs_for_textarea)

        final_attrs = self.build_attrs(attrs)
        del final_attrs['id']

        url = reverse_lazy('django_summernote-editor', kwargs={'id': attrs['id']})
        html += '<iframe id="%s-iframe" src="%s" frameborder="0"%s width="%s" height="%s"></iframe>' \
            % (attrs['id'], url, flatatt(final_attrs), summernote_config['width'], summernote_config['height'])

        return mark_safe(html)
