from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe


class SummernoteWidget(forms.Textarea):
    class Media:
        js = (
            'http://code.jquery.com/jquery-1.9.1.min.js',
            'http://v3.javascriptmvc.com/jquery/dist/jquery.curstyles.min.js',
            '//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js',
            (settings.STATIC_URL or settings.MEDIA_URL) + 'django_summernote/summernote.js',
        )
        css = {
            'screen': (
                '//netdna.bootstrapcdn.com/font-awesome/3.1.1/css/font-awesome.min.css',
                (settings.STATIC_URL or settings.MEDIA_URL) + 'django_summernote/summernote-bootstrap.css',
            )
        }

    def render(self, name, value, attrs=None):
        attrs_for_textarea = attrs.copy()
        attrs_for_textarea['hidden'] = 'true'
        html = super(SummernoteWidget, self).render(name, value, attrs_for_textarea)

        html += '''
        <div id="%(id)s-editor" class="preview">%(content)s</div>
        <script type="text/javascript">
        $("#%(id)s-editor").summernote({ height: 300 });
        $("#%(id)s-editor").parent().find('.note-editable').blur(function() {
            $("#%(id)s").val( $(this).html() );
        });
        </script>
        ''' % {'id': attrs['id'], 'content': value}

        return mark_safe(html)
