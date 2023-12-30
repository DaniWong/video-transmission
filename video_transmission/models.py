from django.db import models
from django.utils.translation import gettext as _

from utils.models import AuditBaseModel


def user_video_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'user_{0}/{1}'.format(instance.created_by.id, filename)


class ProcessedStatus(models.TextChoices):
        TO_PROCESS = "to_process", _("To process'")
        PROCESSING = "processing", _("Processing")
        PROCESSED = "processed", _("Processed")
        PROCESSED_FAILED = "processed_failed", _("Failed process")


class Video(AuditBaseModel):

    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    velocity = models.IntegerField(verbose_name=_('Velocity'))
    video_file = models.FileField(
        verbose_name=_('Video File'), 
        upload_to=user_video_directory_path,
        null=True, blank=False
    )
    video_process_status = models.CharField(
        max_length=20, 
        verbose_name=_('Video status'),
        choices=ProcessedStatus,
        default=ProcessedStatus.TO_PROCESS
    )
    # Processed data type is not specified in requirements then I define a char field
    video_processed_data = models.CharField(max_length=100, verbose_name=_('Video processed data'), null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')
