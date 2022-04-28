from django.urls import path
from .views import PostList, PostDetails


app_name = 'api'

urlpatterns = [
    path('<int:pk>/', PostDetails.as_view(), name="detailcreate"),
    path('', PostList.as_view(), name="listcreate"),
    
]
