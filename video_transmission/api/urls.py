from django.urls import path, include

from rest_framework import routers

from .viewsets import VideoViewSet

app_name = 'api'


router = routers.SimpleRouter()
# router.register(r'video', VideoViewSet)
# not choose router because I just need list, create and post methods according to the requirements

video_list = VideoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

video_detail = VideoViewSet.as_view({
    'get': 'retrieve',
})


urlpatterns = [
    path('video/', video_list, name='video-list'),
    path('video/<int:pk>/', video_detail, name='video-detail'),
]

urlpatterns = router.urls + urlpatterns