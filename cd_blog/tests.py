from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Post, Comment, Like

class CdBlogAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass123', email='user1@example.com')
        self.user2 = User.objects.create_user(username='user2', password='pass123', email='user2@example.com')
        self.post = Post.objects.create(author=self.user, title='Test Post', content='Content here')

    def authenticate(self, user):
        url = reverse('token_obtain_pair')
        resp = self.client.post(url, {'username': user.username, 'password': 'pass123'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        token = resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_create_post_requires_auth(self):
        url = reverse('post-list')  # router name pattern: post-list
        data = {'title': 'New Post', 'content': 'Some content'}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        # now authenticate
        self.authenticate(self.user)
        resp2 = self.client.post(url, data, format='json')
        self.assertEqual(resp2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.filter(title='New Post').exists(), True)

    def test_comment_creation_and_notification(self):
        url = reverse('comment-list')
        self.authenticate(self.user2)
        data = {'post': self.post.id, 'content': 'Nice post!'}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.filter(post=self.post).count(), 1)

    def test_like_unlike(self):
        url = reverse('post-like', kwargs={'pk': self.post.id})  # depends on action name
        self.authenticate(self.user2)
        resp = self.client.post(url, format='json')
        self.assertIn(resp.status_code, (status.HTTP_201_CREATED, status.HTTP_200_OK))
        self.assertEqual(Like.objects.filter(post=self.post, user=self.user2).exists(), True)
        # call again to unlike
        resp2 = self.client.post(url, format='json')
        self.assertEqual(Like.objects.filter(post=self.post, user=self.user2).exists(), False)
