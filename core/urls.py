from turtle import title
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls), #admin site
    path('', include('blog.urls', namespace='blog')),
    path('api/', include('api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # simulate user login in development
    path('api-user/', include('users.urls', namespace='users')), 
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    path('docs/', include_docs_urls(title="BlogAPI")), 
    path('schema', get_schema_view(
        title="DRF API Schema",
        description="General API samples",
        version="1.0.0"
    ), name="openapi-schema"),
    
    
]
