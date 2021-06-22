

from django.urls import path

from .views import AcceptTacView


urlpatterns = [
    path(
        'api-accept/',
        AcceptTacView.as_view(),
        name='tac-api-accept'
    ),
]
