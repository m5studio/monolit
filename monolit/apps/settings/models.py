from django.db import models
from solo.models import SingletonModel


class SiteSettings(SingletonModel):
    site_title       = models.CharField('Site title', max_length=100, blank=True, null=True, help_text='site meta &lt;title&gt;, max 100 chars')
    site_description = models.TextField('Site description', max_length=150, blank=True, null=True, help_text='site meta description, max 150')
    site_email       = models.EmailField('Site Email', max_length=255, blank=True, null=True, help_text='define site main email')
    site_phone       = models.CharField('Site Phone', max_length=50, blank=True, null=True, help_text='define site main email, e.g.: +79784447711')

    def __str__(self):
        return 'Site SEO Settings'

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'
