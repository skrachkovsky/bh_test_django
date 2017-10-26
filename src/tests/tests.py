from time import sleep

from django.test import TestCase

from main.models import Table1


class Test1(TestCase):
    def test_any(self):
        self.assertEqual(1, 1)


class Table1Test(TestCase):
    def setUp(self):
        Table1.objects.create(name='test', value=2, field1='f')

    def test_field1(self):
        t = Table1.objects.get(name='test')
        self.assertEqual(t.field1, 'f1')
