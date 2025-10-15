from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  # anyone can view posts
        return [IsAuthenticated()]  # must be logged in to create/edit/delete

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # Custom endpoint for liking/unliking
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            like.delete()
            return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)
        return Response({'message': 'Post liked'}, status=status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  # anyone can view comments
        return [IsAuthenticated()]  # must be logged in to comment

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
