from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .auth_views import RegisterView
from .profile_views import UserProfileView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),

    # 👇 Custom route for liking a post
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'like_post'}), name='post-like'),
]

