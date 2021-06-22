

from django import forms

from . import conf


class TACAcceptedForm(forms.Form):
    tac = forms.ChoiceField(
        choices=[
            ('accepted', 'accepted'),
        ]
    )


# django >= 1.10
class TACMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request = self.process_request(request)
        response = self.process_response(request)
        return response

    def process_request(self, request):
        form = TACAcceptedForm(request.GET)
        if form.is_valid():
            request.session[conf.TAC_ACCEPTED_SESSION_KEY] = True
        return request

    def process_response(self, request):
        response = self.get_response(request)
        return response


# django <= 1.9.x
class TACMiddlewareLegacy(object):

    def process_request(self, request):
        form = TACAcceptedForm(request.GET)
        if form.is_valid():
            request.session[conf.TAC_ACCEPTED_SESSION_KEY] = True
