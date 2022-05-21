from django.test import TestCase

# Create your tests here.
class TestView(TestCase):
    def test_index(self):
        self.assertEqual(self.client.get('/'), 'Главная страница')
