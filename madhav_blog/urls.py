from django.urls import path
from madhav_blog.views import PostList,PostDetail,ListView

app_name='madhav_blog'
urlpatterns =[
    path('',PostList.as_view(),name='post-list'),
    path('detail/<int:pk>/',PostDetail.as_view(),name='post-detail'),
    path('ajax/likes/',ListView,name='like'),
]