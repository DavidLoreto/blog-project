from django.urls import path

from .views import (
    HomePageView, 
    PostDetailView, 
    DeletePostView,
    NewPostView, 
    EditPostView,
)

urlpatterns = [
    #Home page
    path('', HomePageView.as_view(), name='home'),
    
    #Detailed view of a post
    path(
        'post/<int:pk>/',
        PostDetailView.as_view(), 
        name='post-detail'
    ),

    #Create a new post
    path('post/new/', NewPostView.as_view(), name='post_new'),

    #Edit a post
    path('post/<int:pk>/edit', EditPostView.as_view(), name='post_edit'),

    #Delete a post
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post_delete')
]
