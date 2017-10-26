from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory

from main.models import Table1
from main.views import Index


class Table1Test(TestCase):
    def setUp(self):
        Table1.objects.create(name='test', value=2, field1='f')

    def test_field1(self):
        t = Table1.objects.get(name='test')
        self.assertEqual(t.field1, 'f')


class IndexViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()

        resp = Index.as_view()(request)

        self.assertEqual(resp.status_code, 200)
