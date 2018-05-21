from __future__ import unicode_literals

from django.conf.urls import include, url

from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin


admin.autodiscover()


# SIMPLE PATTERNS
urlpatterns = [
    url(
        r'^tac/',
        include('tac.urls')
    )
]

# i18n PATTERNS
urlpatterns += i18n_patterns(
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
    url(
        r'^',
        include('cms.urls')
    ),
)


# STATIC AND MEDIA FILES FOR DEBUG
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns(settings.STATIC_URL)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
