from django.core.management.base import BaseCommand
from video_transmission.ai import process_pending_videos


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        try:
            process_pending_videos()
            self.stdout.write(
                self.style.SUCCESS('Successfully videos processed')
            )
        except Exception as e:
            self.stdout.write(
                self.style.SUCCESS('Unsuccessfully videos processed %s', str(e))
            )