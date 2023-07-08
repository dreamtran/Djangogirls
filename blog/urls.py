from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the post list view
    path('', views.post_list, name='post_list'),
    # URL pattern for the post detail view, using a dynamic parameter 'pk'
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # URL pattern for creating a new post
    path('post/new/', views.post_new, name='post_new'),
    # URL pattern for editing an existing post, using a dynamic parameter 'pk'
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]