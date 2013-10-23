from django.test import TestCase
from django.core.urlresolvers import reverse_lazy


class DjangoSummernoteTest(TestCase):

    def test_reverse_url_for_summernote(self):
        url = reverse_lazy('django_summernote-editor', kwargs={'id': 'foobar'})
        print url
