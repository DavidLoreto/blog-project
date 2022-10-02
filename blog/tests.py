from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from .models import BlogPost

class BlogTest(TestCase):
    def setUp(self):
        self.test_user = get_user_model().objects.create(
            username='tester',
            email='test@test.com',
            password='secret'
        )

        self.post = BlogPost.objects.create(
            title='test post',
            author=self.test_user,
            content='just a test post'
        )
    

    def test_string_representation(self):
        post = BlogPost(title='Simple title')
        self.assertEqual(str(post), post.title)


    def test_post_content(self):
        #post title
        self.assertEqual(f'{self.post.title}', 'test post')

        #post author
        self.assertEqual(f'{self.post.author}', 'tester')

        #post content
        self.assertEqual(f'{self.post.content}', 'just a test post')


    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
       
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'test post')


    def test_detail_view(self):
        response = self.client.get('/post/detail/1/')
        no_response = self.client.get('post/detail/100000/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        self.assertContains(response, 'test post')
        self.assertContains(response, 'just a test post')
        self.assertContains(response, 'tester')
        
        self.assertEqual(no_response.status_code, 404)
