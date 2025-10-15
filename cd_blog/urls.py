from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('comments/', views.CommentListCreateView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/like/', views.LikePostView.as_view(), name='like-post'),
]
