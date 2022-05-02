from urllib import request
from django.shortcuts import get_object_or_404
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, BasePermission, SAFE_METHODS, IsAuthenticated


# Custom permission
class PostUserWritePermission(BasePermission): 
    message = 'Editing posts is restricted to the author only'
    
    def has_object_permission(self, request, view, obj):
    
        if request.method in SAFE_METHODS:
            return True     
        
        return obj.author == request.user
    


class PostList(generics.ListCreateAPIView):
    """Post list if authenticated"""
    permission_classes = [IsAuthenticated]
    #queryset = Post.postobjects.all() #get the queryset from custom manager
    serializer_class = PostSerializer #parse to JSON


    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)



class PostDetails(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission): 
    """Detail by Post ID"""
    permission_classes = [PostUserWritePermission]
    #queryset = Post.objects.all() #get the queryset
    serializer_class = PostSerializer #parse to JSON
    
    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Post.objects.filter(id=pk)



class PostDetailBySlug(generics.ListAPIView):
    """Detail by slug"""
    serializer_class = PostSerializer #parse to JSON
    
    def get_queryset(self):
        urlSlug= self.kwargs['slug']
        return Post.objects.filter(slug=urlSlug)



""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
