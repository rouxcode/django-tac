from django import forms
from django.contrib import admin

try:
    from text_ckeditor.widgets import CKEditorWidget
except Exception:
    from .widgets import CKEditorWidget

from .. import conf
from ..models import PopupContent


class PopupContentAdminForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = PopupContent
        widgets = {
            'text': CKEditorWidget(conf.CKEDITOR_CONF),
            'language': forms.Select(choices=conf.LANGUAGES)
        }


class PopupContentAdmin(admin.ModelAdmin):

    form = PopupContentAdminForm
    list_display = [
        'get_admin_title',
    ]
