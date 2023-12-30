from django.core.management.base import BaseCommand
from video_transmission.ai import process_failed_videos


class Command(BaseCommand):
    help = "For process failed videos"

    def handle(self, *args, **options):
        try:
            process_failed_videos()
            self.stdout.write(
                self.style.SUCCESS('Successfully videos filed processed')
            )
        except Exception as e:
            self.stdout.write(
                self.style.SUCCESS('Unsuccessfully videos failed processed %s', str(e))
            )