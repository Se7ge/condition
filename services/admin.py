# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from condition.services.models import Services

class ServicesAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Services

class ServicesAdmin(admin.ModelAdmin):
    form = ServicesAdminForm
    list_display = ('name', 'ordernum')

admin.site.register(Services, ServicesAdmin)
