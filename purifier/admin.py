# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from condition.purifier.models import Purifier_Types, Purifier_Producers, Purifier_Products


class ProductsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Purifier_Products


class ProductsAdmin(admin.ModelAdmin):
    form = ProductsAdminForm
    list_display = ('name', 'type_id', 'price', 'area')
    search_fields = ('name', 'description')


class TypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'ordernum')


class ProducersAdmin(admin.ModelAdmin):
    list_display = ('name', 'ordernum')

admin.site.register(Purifier_Types, TypesAdmin)
admin.site.register(Purifier_Products, ProductsAdmin)
admin.site.register(Purifier_Producers, ProducersAdmin)

