from __future__ import unicode_literals

from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse
from django.utils.translation import get_language

from .. import conf
from ..models import PopupContent


register = template.Library()


@register.inclusion_tag('tac/tags/popup.html', takes_context=True)
def tac_popup(context):
    session = context['request'].session
    if session.get(conf.TAC_ACCEPTED_SESSION_KEY):
        return {'show': False}
    language = get_language()
    qs = PopupContent.objects.filter(language=language)
    if qs.count() < 0:
        qs = PopupContent.objects.filter(language=settings.LANGUAGE_CODE)
    if qs.count() < 0:
        qs = PopupContent.objects.all()
    if qs.count() < 0:
        raise ImproperlyConfigured(
            'no popup content in db, please load fixture\n'
            './manage.py tac_load_initial'
        )
    return {
        'object': qs.first(),
        'show': True,
        'url': './?tac=accepted',
        'apiurl': reverse('tac-api-accept'),
    }
