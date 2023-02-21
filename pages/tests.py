from django.test import TestCase # or use SimpleTestCase -a subset of TestCase

# Create your tests here.
# Reverse is useful in testing urls
from django.urls import reverse

from .views import HomePageView

class HomePageTests(TestCase):

    def setUp(self):
        url = reverse('home')

        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        # request for the homepage
        # response = self.client.get('/')
        # if it exist response code is 200 else 400 not found
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):

        #response = self.client.get(reverse('home'))

        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):

        #response = self.client.get('/')

        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_does_not_contain_incorrect_html(self):

        #response = self.client.get('/')

        self.assertNotContains(self.response, 'BleeE')
