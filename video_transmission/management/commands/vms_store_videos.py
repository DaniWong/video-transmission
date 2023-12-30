from django.core.management.base import BaseCommand
from video_transmission.vms import save_video
from video_transmission.models import Video


class Command(BaseCommand):
    help = "For storage videos in VMS"

    def handle(self, *args, **options):
        try:
            videos = Video.objects.all()
            save_video(videos)
            self.stdout.write(
                self.style.SUCCESS('Successfully saved videos from VMS')
            )
        except Exception as e:
            self.stdout.write(
                self.style.SUCCESS('Unsuccessfully retrieve videos from VMS %s', str(e))
            )
