from django.db import models


class SiteSeoSettings(models.Model):
    site_title       = models.CharField('Site title', max_length=100, help_text='site meta &lt;title&gt;, max 100 chars')
    site_description = models.TextField('Site description', max_length=150, help_text='site meta description, max 150')

    def __str__(self):
        return 'Site SEO Settings'

    class Meta:
        verbose_name = 'Site SEO Setting'
        verbose_name_plural = 'Site SEO Settings'


class SiteContactSettings(models.Model):
    site_email = models.EmailField('Site Email', max_length=255, help_text='define site main email')
    site_phone = models.CharField('Site Phone', max_length=50, help_text='define site main email, e.g.: 79784447711')

    def __str__(self):
        return 'Site Contacts Settings'

    class Meta:
        verbose_name = 'Site Contacts Setting'
        verbose_name_plural = 'Site Contacts Settings'
