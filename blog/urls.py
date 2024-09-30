from django.urls import path 
from .views import post_list, post_detail, create_post, PostUpdate, sign_up, post_delete, comment_delete, comment_edit, index


urlpatterns = [
    path('index/', index, name='index'),
    path('sign_up', sign_up, name='sign_up'),
    path('news/', post_list, name='news'),
    path('new', create_post, name='blog_new'),
    path('<int:pk>', post_detail, name='blog_detail'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='blog_edit'),
    path('<int:post_id>/delete', post_delete, name='blog_delete'),
    path('<int:post_id>/edit_comment/<int:comment_id>',comment_edit, name='blog_edit'),
    path('<int:post_id>/delete_comment/<int:comment_id>',comment_delete, name='blog_delete'),
]
