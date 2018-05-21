from __future__ import unicode_literals

from django.conf.urls import url

from .views import AcceptTacView


urlpatterns = [
    url(
        r'^api-accept/$',
        AcceptTacView.as_view(),
        name='tac-api-accept'
    ),
]
