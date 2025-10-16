from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # ✅ Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author__username']             # filter posts by author
    search_fields = ['title', 'content']                # search in title or content
    ordering_fields = ['created_at']                    # sort by date
    ordering = ['-created_at']

    # ✅ Attach logged-in user as author automatically
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # ✅ Custom like/unlike endpoint
    @action(detail=True, methods=['post'], url_path='like')
    def like_post(self, request, pk=None):
        """
        Toggle like/unlike for a post.
        """
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        # Create or remove like
        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            like.delete()
            return Response({'message': 'Post unliked.'}, status=status.HTTP_200_OK)

        return Response({'message': 'Post liked!'}, status=status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

