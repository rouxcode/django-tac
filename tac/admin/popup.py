from __future__ import unicode_literals

from django import forms
from django.contrib import admin

from text_ckeditor.widgets import CKEditorWidget

from .. import conf
from ..models import PopupContent


class PopupContentAdminForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = PopupContent
        widgets = {
            'text': CKEditorWidget(conf.CKEDITOR_CONF)
        }


class PopupContentAdmin(admin.ModelAdmin):

    form = PopupContentAdminForm
    list_display = [
        'get_admin_title',
    ]
