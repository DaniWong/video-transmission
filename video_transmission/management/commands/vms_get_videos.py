from django.core.management.base import BaseCommand
from video_transmission.vms import retieve_videos


class Command(BaseCommand):
    help = "For retrieve videos from VMS"

    def handle(self, *args, **options):
        try:
            videos = retieve_videos()
            self.stdout.write(
                self.style.SUCCESS('Successfully retrive videos from VMS')
            )
        except Exception as e:
            self.stdout.write(
                self.style.SUCCESS('Unsuccessfully retrieve videos from VMS %s', str(e))
            )