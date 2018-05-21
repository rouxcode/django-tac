from __future__ import unicode_literals

from django.contrib import admin

from .link import PopupLink, PopupLinkAdmin
from .popup import PopupContent, PopupContentAdmin


admin.site.register(PopupContent, PopupContentAdmin)
admin.site.register(PopupLink, PopupLinkAdmin)
