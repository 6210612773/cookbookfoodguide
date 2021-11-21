from django.http import request
from django.shortcuts import get_object_or_404
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from recipe.models import ingredient , recipe ,order,search, petition , Addrecipe ,Comment
from django.contrib.auth.hashers import make_password
password = make_password('1234')

# Create your tests here.

class RecipeModelTestCase(TestCase):
    def setUp(self):
        User.objects.create(username= 'user1', password=password,email= 'user1@example.com')
        menu1= recipe.objects.create(menu='soup',type='meat',price=0.0,pic='static/images/bg.png')
        menu2 = recipe.objects.create(menu='porksoup',type='halal',price=20,pic='static/images/bg.png') 

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

    def test_admin_petition(self):
        c = Client()
        response = c.get(reverse('recipe:petition'))
        self.assertEqual(response.status_code, 200)

    def test_admin_addmenu(self):
        c = Client()
        response = c.get(reverse('recipe:addmenu'))
        self.assertEqual(response.status_code, 200)

    def test_complete_recipe(self):
        c = Client()
        response = c.get(reverse('recipe:complete'))
        self.assertEqual(response.status_code, 200)


    def test_admin_order(self):
        c = Client()
        response = c.get(reverse('recipe:order'))
        self.assertEqual(response.status_code, 200)


    def test_menu_recipe(self):
        c = Client()
        recipe1 = recipe.objects.get(menu='soup') 
        response = c.get(reverse('recipe:menu', args=(recipe1.id,)))
        self.assertEqual(response.status_code, 200)
        recipe2 = recipe.objects.get(menu='porksoup') 
        response = c.get(reverse('recipe:menu', args=(recipe2.id,)))
        self.assertEqual(response.status_code, 302)


    def test_menu_recipe_with_authenticate(self):
        c = Client()
        user = User.objects.get(username='user1')
        c.force_login(user)
        recipe1 = recipe.objects.get(menu='soup') 
        response = c.get(reverse('recipe:menu', args=(recipe1.id,)))
        self.assertEqual(response.status_code, 200)
        recipe2 = recipe.objects.get(menu='porksoup') 
        response = c.get(reverse('recipe:menu', args=(recipe2.id,)))
        self.assertEqual(response.status_code, 200)


    def test_recipe_purchased(self):
        c = Client()
        response = c.get(reverse('recipe:purchased'))
        self.assertEqual(response.status_code, 200)


    def test_myrecipe(self):
        c = Client()
        response = c.get(reverse('recipe:myrecipe'))
        self.assertEqual(response.status_code, 200)


    def test_recipe_mylike(self):
        c = Client()
        response = c.get(reverse('recipe:mylike'))
        self.assertEqual(response.status_code, 200)

    def test_search_with_authenticate(self):
        c = Client()
        user = User.objects.get(username='user1')
        c.force_login(user)
        response = c.get(reverse('recipe:search'))
        self.assertEqual(response.status_code, 200)

    def test_search_without_authenticate(self):
        c = Client()
        response = c.get(reverse('recipe:search'))
        self.assertEqual(response.status_code, 200)

    def test_like_button(self):
        c = Client()
        user = User.objects.get(username='user1')
        c.force_login(user)
        recipe1 = recipe.objects.get(menu='soup')
        response = c.get(reverse('recipe:like', args=(recipe1.id,)))
        self.assertEqual(response.status_code, 302)
        response = c.get(reverse('recipe:like', args=(recipe1.id,))) 



