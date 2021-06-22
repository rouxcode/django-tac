

from django import forms

from text_ckeditor.admin import DjangoLinkAdmin

from .. import conf
from ..models import PopupLink


class PopupLinkAdminForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = PopupLink
        widgets = {}


class PopupLinkAdmin(DjangoLinkAdmin):

    fieldsets = conf.LINK_FIELDSETS
    form = PopupLinkAdminForm

    class Media:
        css = {
            'all': ['admin/links/css/link.ckeditor.css']
        }
        js = (
            'admin/links/js/link.type.js',
        )

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "link_type":
            # add link_type choices defined by the actual model
            db_field.choices = self.model.link_type_choices
            db_field.widget = forms.Select
        return super(PopupLinkAdmin, self).formfield_for_dbfield(
            db_field,
            **kwargs
        )
