# from django.test import TestCase

# Create your tests here.
# ==============================================
from django.test import TestCase, SimpleTestCase
from django.urls import reverse


# class CoreTests(TestCase):
# class CoreTests(SimpleTestCase):
#     def test_sample(self):
#         assert 1 == 1
#
#     def test_homepage_status_code(self):
#         # response = self.client.get(reverse('homepage'))
#         response = self.client.get('/')
#
#         print( response.status_code )
#         # response = self.client.get(reverse('homepage'))
#         # response = self.client.get('/')
#         # self.assertEqual(response.status_code, 200)
#         # self.assertEqual(201, 200)


class TestCore(TestCase):
# class TestCore(SimpleTestCase):

    def test_sample(self):
        assert 1 == 1

    def test_homepage(self):
        # print(reverse('homepage'))
        # response = self.client.get('/')
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
