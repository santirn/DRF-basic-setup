from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category

class Test_Create_Post(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create(username = "testuser1", password="testuser1")
        testPost = Post.objects.create(category_id = 1, tittle ="Test Post Tittle", excerpt ="excerpt",content="Test Post Content",slug="test-post-tittle", author_id = 1, status="published")

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        tittle = f'{post.tittle}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(excerpt, 'excerpt')
        self.assertEqual(author, 'testuser1')
        self.assertEqual(tittle, 'Test Post Tittle')
        self.assertEqual(content, 'Test Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Test Post Tittle')
        self.assertEqual(str(cat), 'django')
