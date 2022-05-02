from django.urls import path
from .views import PostList, PostDetails, PostDetailBySlug


app_name = 'api'

urlpatterns = [
    path('posts/<int:pk>/', PostDetails.as_view(), name="detailcreate"),
    path('posts/<str:slug>/', PostDetailBySlug.as_view(), name="PostBySlug"),
    path('', PostList.as_view(), name="listcreate"),
    
]