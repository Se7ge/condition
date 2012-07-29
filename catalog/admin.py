# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from condition.catalog.models import Types, Producers, Products

class ProductsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
	model = Products

class ProductsAdmin(admin.ModelAdmin):
    form = ProductsAdminForm
    list_display = ('name', 'price', 'area')
    search_fields = ('name', 'description')

class ProducersAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
	model = Producers

class ProducersAdmin(admin.ModelAdmin):
    form = ProducersAdminForm
    list_display = ('name', 'ordernum')

class TypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'ordernum')

admin.site.register(Types, TypesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Producers, ProducersAdmin)
