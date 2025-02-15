from django.urls import include, path
from rest_framework.authtoken import views

from rest_framework import routers

from api.views import PostViewSet, GroupViewSet, CommentViewSet


router = routers.SimpleRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),    
]
