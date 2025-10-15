from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import PostSerializer, CommentSerializer

class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        posts = user.posts.all().order_by('-created_at')
        comments = user.comments.all().order_by('-created_at')

        return Response({
            "username": user.username,
            "email": user.email,
            "total_posts": posts.count(),
            "total_comments": comments.count(),
            "posts": PostSerializer(posts, many=True).data,
            "comments": CommentSerializer(comments, many=True).data
        })
