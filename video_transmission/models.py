from django.db import models
from django.utils.translation import gettext as _

from utils.models import AuditBaseModel


def user_video_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'user_{0}/{1}'.format(instance.created_by.id, filename) 


class Video(AuditBaseModel):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    velocity = models.IntegerField(verbose_name=_('Velocity'))
    video_file = models.FileField(
        verbose_name=_('Video File'), 
        upload_to=user_video_directory_path,
        null=True, blank=False
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')
