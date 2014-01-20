from django.test import TestCase
from django.core.urlresolvers import reverse


class DjangoSummernoteTest(TestCase):

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
        html = widget.render('foobar', 'lorem ipsum', attrs={'id': 'foobar'})
        url = reverse('django_summernote-editor', kwargs={'id': 'foobar'})

        assert url in html
        assert 'id="foobar"' in html
