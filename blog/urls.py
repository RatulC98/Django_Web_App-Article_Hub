from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView,
                    PostDeleteView, UserPostListView, AddCommentView, like_view,
                    delete_comment, latest_posts, top_posts)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('announcements/', views.announcements, name='blog-announcements'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='post-comment'),
    path('like/<int:pk>/', like_view, name='like-post'),
    path('comment/delete/', delete_comment, name='delete_comment'),
    path('latest-posts/', latest_posts, name='latest-posts'),
    path('top-posts/', top_posts, name='top-posts'),
]
