from __future__ import unicode_literals

from django.contrib import admin

try:
    from .link import PopupLink, PopupLinkAdmin
    admin.site.register(PopupLink, PopupLinkAdmin)
except Exception:
    pass

from .popup import PopupContent, PopupContentAdmin
admin.site.register(PopupContent, PopupContentAdmin)
