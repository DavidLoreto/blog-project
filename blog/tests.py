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


    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')


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
        response = self.client.get('/post/1/')
        no_response = self.client.get('post/100000/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        self.assertContains(response, 'test post')
        self.assertContains(response, 'just a test post')
        self.assertContains(response, 'tester')
        
        self.assertEqual(no_response.status_code, 404)


    def test_create_post(self):
        response = self.client.get('/post/new/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_new.html')


    def test_edit_post(self):
        response = self.client.post(reverse('post_edit', args='1'),
            {
                'title': 'Updated title',
                'content': 'Updated text.'
            }
        )

        self.assertEqual(response.status_code, 302)

    
    def test_delete_post(self):
        response = self.client.get('/post/1/delete')

        self.assertEqual(response.status_code, 301)
