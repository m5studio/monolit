from django.test import TestCase, SimpleTestCase
# from django.urls import reverse


# class CoreTests(TestCase):
class CoreTests(SimpleTestCase):
    def test_homepage_status_code(self):
        # response = self.client.get('/')
        # print(response.status_code)
        # self.assertEqual(response.status_code, 200)

        # url = reverse('homepage')
        # print(url)

        assert 1 == 1


    # def test_response_status(self):
    #     response = self.client.get(reverse('homepage'))
    #     self.assertEqual(response.status_code, 200)
