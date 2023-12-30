from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from .models import Video
from .ai import process_videos, ProcessedStatus

User = get_user_model()

class AiVideoTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='root')
        Video.objects.create(
            title="Kitchen", description="Example", 
            velocity=2, created_by=user, updated_by=user
        )
        Video.objects.create(
            title="Garden", description="Example garden", 
            velocity=1, created_by=user, updated_by=user
        )

    def test_videos_processed(self):
        videos = Video.objects.all()
        process_videos(videos)
        for v in Video.objects.all():
            self.assertEqual(v.video_process_status, ProcessedStatus.PROCESSED)


class VideoApiListTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='root', password='root')
        Video.objects.create(
            title="Kitchen", description="Example", 
            velocity=2, created_by=user, updated_by=user
        )
        Video.objects.create(
            title="Garden", description="Example garden", 
            velocity=1, created_by=user, updated_by=user
        )

    def test_video_api_list_auth_failed(self):
        client = APIClient()
        url = '/video-transmission/api/v1/video/'
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, 401)
