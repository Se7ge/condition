# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from condition.ventilation.models import Ventilation_Types, Ventilation_Products

class ProductsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
	model = Ventilation_Products

class ProductsAdmin(admin.ModelAdmin):
    form = ProductsAdminForm
    list_display = ('name', 'type_id', 'price', 'area')
    search_fields = ('name', 'description')

class TypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'ordernum')

admin.site.register(Ventilation_Types, TypesAdmin)
admin.site.register(Ventilation_Products, ProductsAdmin)

