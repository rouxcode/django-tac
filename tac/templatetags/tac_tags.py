

from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
try:
    from django.urls import reverse
except Exception:
    from django.core.urlresolvers import reverse
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
    qs = PopupContent.objects.filter(
        site_id=settings.SITE_ID,
        language=language,
    )
    if qs.count() < 0:
        qs = PopupContent.objects.filter(
            site_id=settings.SITE_ID,
            language=settings.LANGUAGE_CODE,
        )
    if qs.count() < 0:
        qs = PopupContent.objects.filter(
            site_id=settings.SITE_ID
        )
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


@register.inclusion_tag('tac/tags/popup_no_ckeditor.html', takes_context=True)
def tac_popup_no_ckeditor(context):
    return tac_popup(context)
