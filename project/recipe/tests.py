from django.http import request
from django.shortcuts import get_object_or_404
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from recipe.models import ingredient , recipe


# Create your tests here.

class RecipeModelTestCase(TestCase):

    def test_index_recipe(self):
        c = Client()
        response = c.get(reverse('recipe:index'))
        self.assertEqual(response.status_code, 200)

    
    def test_meat_recipe(self):
        c = Client()
        response = c.get(reverse('recipe:meat'))
        self.assertEqual(response.status_code, 200)

    def test_norm_recipe(self):
        c = Client()
        response = c.get(reverse('recipe:norm'))
        self.assertEqual(response.status_code, 200)

    def test_hal_recipe(self):
        c = Client()
        response = c.get(reverse('recipe:hal'))
        self.assertEqual(response.status_code, 200)

    def test_bev_recipe(self):
        c = Client()
        response = c.get(reverse('recipe:bev'))
        self.assertEqual(response.status_code, 200)
    
    def test_oco_recipe(self):
        c = Client()
        response = c.get(reverse('recipe:oco'))
        self.assertEqual(response.status_code, 200)

    def test_vegy_recipe(self):
        c = Client()
        response = c.get(reverse('recipe:vegy'))
        self.assertEqual(response.status_code, 200)

    def test_app_recipe(self):
        c = Client()
        response = c.get(reverse('recipe:app'))
        self.assertEqual(response.status_code, 200)

    def test_mode_recipe(self):
        c = Client()
        response = c.get(reverse('recipe:mode'))
        self.assertEqual(response.status_code, 200)

    def test_menu_recipe(self):
        c = Client()
        recipe1 = recipe.objects.create(menu='soup',type='meat') 
        response = c.get(reverse('recipe:menu', args=(recipe1.id,)))
        recipe2 = recipe.objects.create(menu='soup',type='halal',price=20) 
        response = c.get(reverse('recipe:menu', args=(recipe1.id,)))
        response = c.get(reverse('recipe:menu', args=(recipe2.id,)))
        self.assertEqual(response.status_code, 200)


    def test_confirm_recipe(self):
        c = Client()
        response = c.get(reverse('recipe:confirm'))
        self.assertEqual(response.status_code, 200)
