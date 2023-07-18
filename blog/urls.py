from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    # URL pattern for the post list view
    path('', views.post_list, name='post_list'),
    # URL pattern for the post detail view, using a dynamic parameter 'pk'
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # URL pattern for creating a new post
    path('post/new/', views.post_new, name='post_new'),
    # URL pattern for editing an existing post, using a dynamic parameter 'pk'
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]