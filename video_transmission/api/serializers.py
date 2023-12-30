from rest_framework import serializers

from utils.mixins import AuditableSerializerMixin

from ..models import Video


class VideoSerializer(AuditableSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'velocity', 'video_file']
        # This is because video file was added after early version of video model
        extra_kwargs = {"video_file": {"required": True, "allow_null": False}}
