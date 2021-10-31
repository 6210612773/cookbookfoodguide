from django.http import request
from django.shortcuts import get_object_or_404
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.




class AboutModelTestCase(TestCase):

    def test_index_about(self):
        c = Client()
        response = c.get(reverse('about:index'))
        self.assertEqual(response.status_code, 200)
    
    def test_ER_about(self):
        c = Client()
        response = c.get(reverse('about:ER'))
        self.assertEqual(response.status_code, 200)

    def test_Goals_about(self):
        c = Client()
        response = c.get(reverse('about:Goals'))
        self.assertEqual(response.status_code, 200)

    def test_Personas_about(self):
        c = Client()
        response = c.get(reverse('about:Personas'))
        self.assertEqual(response.status_code, 200)

    def test_stories_about(self):
        c = Client()
        response = c.get(reverse('about:stories'))
        self.assertEqual(response.status_code, 200)
    def test_Sitemap_about(self):
        c = Client()
        response = c.get(reverse('about:Sitemap'))
        self.assertEqual(response.status_code, 200)
    
    def test_Descriptions_about(self):
        c = Client()
        response = c.get(reverse('about:Descriptions'))
        self.assertEqual(response.status_code, 200)

    def test_Wireframes_about(self):
        c = Client()
        response = c.get(reverse('about:Wireframes'))
        self.assertEqual(response.status_code, 200)

    def test_non_functional_about(self):
        c = Client()
        response = c.get(reverse('about:non_funtional'))
        self.assertEqual(response.status_code, 200)