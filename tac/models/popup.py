from django.db import models
from django.utils.translation import ugettext_lazy as _


class PopupContent(models.Model):

    name = models.CharField(
        max_length=150,
        verbose_name=_('Name'),
    )
    site = models.ForeignKey(
        'sites.Site',
        default=1,
        on_delete=models.CASCADE,
        verbose_name=_('Site'),
    )
    language = models.CharField(
        max_length=10,
        default='de',
        verbose_name=_('Language'),
    )
    text = models.TextField(
        default='',
        verbose_name=_('Text'),
    )
    button_label = models.CharField(
        max_length=150,
        blank=True,
        default='',
        verbose_name=_('Button label'),
    )

    class Meta:
        ordering = ['language', '-id']
        verbose_name = _('Popup Content')
        verbose_name_plural = _('Popup Content')

    def __str__(self):
        return '{}'.format(self.name)

    def get_button_label(self):
        label = self.button_label or _('I have understood')
        return '{}'.format(label)

    def get_admin_title(self):
        return '{}: {}'.format(self.language, self.name)
    get_admin_title.short_description = _('Title')
