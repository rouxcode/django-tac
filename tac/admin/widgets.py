from __future__ import unicode_literals

from django import forms


class CKEditorWidget(forms.Textarea):

    def __init__(self, *args, **kwargs):
        try:
            kwargs.popu('conf')
        except Exception:
            pass

        super(CKEditorWidget, self).__init__(*args, **kwargs)
