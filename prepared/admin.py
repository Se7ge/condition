# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from condition.prepared.models import Prepared

class PreparedAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Prepared

class PreparedAdmin(admin.ModelAdmin):
    form = PreparedAdminForm
    list_display = ('name', 'ordernum')

admin.site.register(Prepared, PreparedAdmin)
