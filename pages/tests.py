from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        #response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        #response = self.client.get(reverse('home'))
        self.assertEqual(self.response.status_code, 200)
    
    def test_template_homepage(self):
        #response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'home.html', '_base.html')
        #self.assertTemplateNotUsed(response, 'home.html')
        #self.assertTemplateNotUsed(response, '_base.html')

    def test_homepage_contains_correct_html(self): # new
        #response = self.client.get('/')
        self.assertContains(self.response, 'Home Page')
    
    def test_homepage_does_not_contain_incorrect_html(self): # new
        #response = self.client.get('/')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')