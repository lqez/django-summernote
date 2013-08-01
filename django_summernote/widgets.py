from django import forms
from django.core.urlresolvers import reverse_lazy
from django.utils.safestring import mark_safe


class SummernoteWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        attrs_for_textarea = attrs.copy()
        attrs_for_textarea['hidden'] = 'true'
        html = super(SummernoteWidget, self).render(name, value, attrs_for_textarea)

        url = reverse_lazy('django_summernote-editor', args=(attrs['id'],))
        html += '<iframe src="%s" width="720" height="320" frameborder="0"></iframe>' % url

        return mark_safe(html)
