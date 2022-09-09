from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='followers')
router_v1.register(r'^posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')

token_patern = [
    path('create/', TokenObtainPairView.as_view(), name='token_create'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/jwt/', include(token_patern)),
]
