from django.db import models
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _

from cms.models.fields import PageField


class PopupLink(models.Model):

    link_type_choices = [
        ('', _('---')),
        ('link_cms_page', _('Seite')),
        ('link_url', _('URL')),
    ]
    link_types = [k for k, v in link_type_choices]

    link_types_absolute_url = [
        'link_cms_page',
    ]

    name = models.CharField(
        max_length=150,
        verbose_name=_('Name')
    )

    link_type = models.CharField(
        max_length=30,
        blank=True,
        choices=link_type_choices,
        default='',
        verbose_name=_('Link type')
    )

    link_cms_page = PageField(
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_set',
        verbose_name=_('Page'),
    )
    link_url = models.URLField(
        max_length=255,
        blank=True,
        default='',
        verbose_name=_('URL'),
    )

    def __str__(self):
        return '{}'.format(self.name or self.get_link())

    def get_email(self):
        return ''

    def get_link(self):
        href = ''
        try:
            field = getattr(self, self.link_type, None)
            link_type = getattr(self, 'link_type', None)
        except Exception:
            return href
        if link_type and field:
            if link_type in self.link_types_absolute_url:
                href = field.get_absolute_url()
            elif link_type == 'link_url':
                href = self.link_url
        return href

    def get_link_type(self):
        link_type = self.link_type
        if not link_type:
            # Fallback if the link_type property isn't set
            for field in self.link_types:
                # get the first link with a value and return the type
                value = getattr(self, field, None)
                if value:
                    link_type = field
                    break
        return link_type

    def get_target(self):
        if not self.link_cms_page and (self.get_filer_file() or self.link_url):
            return '_blank'
        else:
            return ''

    def get_html_attrs(self):
        attrs = ''
        if self.get_link_type() == 'link_url':
            attrs = ' target="_blank" rel="noreferrer"'
        return mark_safe(attrs)

    @property
    def is_email(self):
        return False
