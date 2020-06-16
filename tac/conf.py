from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


TAC_ACCEPTED_SESSION_KEY = 'tac_accepted'

LANGUAGES = getattr(
    settings,
    'LANGUAGES',
    [
        ('de', 'De'),
        ('en', 'En'),
        ('fr', 'Fr'),
        ('it', 'It'),
        ('es', 'Es'),
    ]
)


CKEDITOR_CONF = {
    'height': 100,
    'width': '100%',
    'skin': 'moono-lisa',
    'uiColor': '#ffffff',
    'extraPlugins': 'djangolink',
    'toolbar': [
        ['Bold'],
        ['DjangoLink', 'Unlink'],
    ],
}


LINK_FIELDSETS = [
    (_('Target'), {
        'classes': [
            'section',
            'link',
            'page-anchors-js',
        ],
        'fields': [
            'link_type',
            'link_cms_page',
            'link_url',
        ],
    }),
]
