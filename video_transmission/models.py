from django.db import models
from django.utils.translation import gettext as _

from utils.models import AuditBaseModel


class Video(AuditBaseModel):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    velocity = models.IntegerField(verbose_name=_('Velocity'))

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')
