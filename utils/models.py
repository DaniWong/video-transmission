from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class AuditBaseModel(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Created by'), related_name='%(class)s_requests_created')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_("Creation date"))

    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Updated by'), related_name='%(class)s_requests_updated') 
    updated_on = models.DateTimeField(auto_now=True, verbose_name=_("Modify date"))

    class Meta:
        abstract = True
