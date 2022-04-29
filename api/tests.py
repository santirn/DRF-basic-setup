from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from blog.models import Post, Category

class PostTests(APITestCase):
    
    def test_view_post(self):
        url = reverse('api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_create_post(self):
        
        self.category = Category.objects.create(name='TEST CATEGORY')
        self.testuser1 = User.objects.create_superuser(username = "testuser1", password="testuser1")
        
        self.client.login(username=self.testuser1.username,
                          password="testuser1")
        
        data =  {
            "tittle": "TESTING TITLE",
            "author": 1,
            "excerpt": "Testing excerpt",
            "content": "Testing content",
        }
        
        url = reverse('api:listcreate')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_post_update(self):
        
        client = APIClient()
        
        self.test_category = Category.objects.create(name="django test")
        self.testuser1 = User.objects.create_user(username = "testuser1", password="testuser1")
        self.testuser2 = User.objects.create_user(username = "testuser2", password="testuser2")
        test_post = Post.objects.create(category_id=1, tittle="test tittle", excerpt="test excerpt", content="test content", slug="test-tittle", status="published", author_id=1)
        test_post2 = Post.objects.create(category_id=1, tittle="test tittle2", excerpt="test excerpt2", content="test content2", slug="test-tittle", status="published", author_id=2)
     
        client.login(username=self.testuser1.username, password="testuser1")
        url = reverse(('api:detailcreate'), kwargs={'pk': 1})
        data =  {
            "tittle": "put TESTING TITLE",
            "author": 1,
            "excerpt": "put Testing excerpt",
            "content": "put Testing content",
            "status" : "published"
        }

        response = client.put(url, data, format="json")
        print(response.data) #errors detail
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
