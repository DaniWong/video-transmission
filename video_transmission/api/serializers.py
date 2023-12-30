from rest_framework import serializers

from utils.mixins import AuditableSerializerMixin

from ..models import Video


class VideoSerializer(AuditableSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'velocity']
