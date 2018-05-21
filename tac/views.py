from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.generic import View

from .import conf


class AcceptTacView(View):

    def get(self, request, *args, **kwargs):
        accepted = request.session.get(conf.TAC_ACCEPTED_SESSION_KEY, False)
        if not accepted:
            request.session[conf.TAC_ACCEPTED_SESSION_KEY] = True
        data = {
            'message': 'ok',
        }
        return JsonResponse(data)
