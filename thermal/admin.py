# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from condition.thermal.models import Thermal_Types, Thermal_Products

class ProductsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
	model = Thermal_Products

class ProductsAdmin(admin.ModelAdmin):
    form = ProductsAdminForm
    list_display = ('name', 'type_id', 'price', 'area')
    search_fields = ('name', 'description')

class TypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'ordernum')

admin.site.register(Thermal_Types, TypesAdmin)
admin.site.register(Thermal_Products, ProductsAdmin)

