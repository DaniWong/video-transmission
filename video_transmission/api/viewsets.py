from rest_framework import viewsets

from utils.mixins import AuditableViewSetMixin

from .serializers import VideoSerializer
from ..models import Video


class VideoViewSet(AuditableViewSetMixin, viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

