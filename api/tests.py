from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category

class PostTests(APITestCase):
    
    def test_view_post(self):
        url = reverse('api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def create_post(self):
        
        self.testuser1 = User.objects.create(username = "testuser1", password="testuser1")
        
        data =  {
            "tittle": "TESTING TITLE",
            "author": 1,
            "excerpt": "Testing excerpt",
            "content": "Testing content",
        }
        
        url = reverse('api:listcreate')
        response = self.client(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
