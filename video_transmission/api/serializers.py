from rest_framework import serializers

from utils.mixins import AuditableSerializerMixin

from ..models import Video


class VideoSerializer(AuditableSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'velocity', 'video_file', 'video_process_status', 'video_processed_data']
        # This is because video file was added after early version of video model
        extra_kwargs = {
            "video_file": {"required": True, "allow_null": False},
            "video_process_status": {"read_only": True},
            "video_processed_data": {"read_only": True},
        }
