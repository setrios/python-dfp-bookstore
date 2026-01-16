from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView

# Create your tests here.

class HomepageTest(SimpleTestCase):
    # setup before testing
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    # testing urls
    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    # testing templates
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    # testing html content
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'checkout')

    # check right view function used
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)