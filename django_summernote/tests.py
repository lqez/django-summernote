from django.contrib.admin.sites import AdminSite
from django.core.urlresolvers import reverse
from django.test import TestCase
from django_summernote.settings import summernote_config
from imp import reload


class DjangoSummernoteTest(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_base(self):
        self.assertTrue(True)

    def test_url(self):
        url = reverse('django_summernote-editor', kwargs={'id': 'foobar'})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'summernote.min.js')
        self.assertContains(response, 'summernote.css')

    def test_widget(self):
        from django_summernote.widgets import SummernoteWidget

        widget = SummernoteWidget()
        html = widget.render(
            'foobar', 'lorem ipsum', attrs={'id': 'id_foobar'}
        )
        url = reverse('django_summernote-editor', kwargs={'id': 'id_foobar'})

        assert url in html
        assert 'id="id_foobar"' in html

    def test_widget_inplace(self):
        from django_summernote.widgets import SummernoteInplaceWidget

        widget = SummernoteInplaceWidget()
        html = widget.render(
            'foobar', 'lorem ipsum', attrs={'id': 'id_foobar'}
        )

        assert 'summernote' in html

    def test_form(self):
        from django import forms
        from django_summernote.widgets import SummernoteWidget

        class SimpleForm(forms.Form):
            foobar = forms.CharField(widget=SummernoteWidget())

        f = SimpleForm()
        html = f.as_p()
        url = reverse('django_summernote-editor', kwargs={'id': 'id_foobar'})

        assert url in html
        assert 'id="id_foobar"' in html

    def test_attachment(self):
        import os
        url = reverse('django_summernote-upload_attachment')

        with open(__file__, 'rb') as fp:
            response = self.client.post(url, {'files': [fp]})
            self.assertEqual(response.status_code, 200)
            self.assertContains(
                response, '"name": "%s"' % os.path.basename(__file__))
            self.assertContains(response, '"url": ')
            self.assertContains(response, '"size": ')

    def test_attachment_with_custom_storage(self):
        summernote_config['attachment_storage_class'] = \
            'django.core.files.storage.DefaultStorage'

        # reloading module to apply custom stroage class
        from django_summernote import models
        reload(models)

        url = reverse('django_summernote-upload_attachment')

        with open(__file__, 'rb') as fp:
            response = self.client.post(url, {'files': [fp]})
            self.assertEqual(response.status_code, 200)

    def test_attachment_with_bad_storage(self):
        from django.core.exceptions import ImproperlyConfigured

        # ValueError
        summernote_config['attachment_storage_class'] = \
            'wow_no_dot_storage_class_name'
        with self.assertRaises(ImproperlyConfigured):
            from django_summernote import models
            reload(models)

        # ImportError
        summernote_config['attachment_storage_class'] = \
            'wow.such.fake.storage'
        with self.assertRaises(ImproperlyConfigured):
            from django_summernote import models
            reload(models)

        # AttributeError
        summernote_config['attachment_storage_class'] = \
            'django.core.files.storage.DogeStorage'

        with self.assertRaises(ImproperlyConfigured):
            from django_summernote import models
            reload(models)

    def test_attachment_bad_request(self):
        url = reverse('django_summernote-upload_attachment')
        response = self.client.get(url)

        self.assertNotEqual(response.status_code, 200)

    def test_attachment_no_attachment(self):
        url = reverse('django_summernote-upload_attachment')
        response = self.client.post(url)

        self.assertNotEqual(response.status_code, 200)

    def test_attachment_filesize_exceed(self):
        import os

        url = reverse('django_summernote-upload_attachment')
        size = os.path.getsize(__file__)
        old_limit = summernote_config['attachment_filesize_limit']
        summernote_config['attachment_filesize_limit'] = size - 1

        with open(__file__, 'rb') as fp:
            response = self.client.post(url, {'files': [fp]})
            self.assertNotEqual(response.status_code, 200)

        summernote_config['attachment_filesize_limit'] = old_limit

    def test_admin_model(self):
        from django.db import models
        from django_summernote.admin import SummernoteModelAdmin
        from django_summernote.admin import SummernoteInlineModelAdmin
        from django_summernote.widgets import SummernoteWidget

        class SimpleParentModel(models.Model):
            foobar = models.TextField()

        class SimpleModel(models.Model):
            foobar = models.TextField()
            parent = models.ForeignKey(SimpleParentModel)

        class SimpleModelInline(SummernoteInlineModelAdmin):
            model = SimpleModel

        class SimpleParentModelAdmin(SummernoteModelAdmin):
            inlines = [SimpleModelInline]

        ma = SimpleParentModelAdmin(SimpleParentModel, self.site)

        assert isinstance(
            ma.get_form(None).base_fields['foobar'].widget,
            SummernoteWidget
        )
