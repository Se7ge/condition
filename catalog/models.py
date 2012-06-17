#-*- coding: utf-8 -*-
from django.db import models
from django.db import utils

import datetime
from ckeditor.widgets import CKEditorWidget

class Types(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name=u'Название')
    description = models.TextField(blank=True, verbose_name=u'Описание', widget=CKEditorWidget())
    
    def __unicode__(self):
	return self.name
    
    class Meta:
        ordering = ["name"]

class Producers(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name=u'Производитель')
    decription = models.TextFiled(blank=True, verbose_name=u'Описание', widget=CKEditorWidget())

    def __unicode__(self):
	return self.name

    class Meta:
	ordering = ["name"]
	verbose_name = u'Производитель'

class Products(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name=u'Название')
    producer_id = models.ForeignKey(Producers)
    type_id = models.ForeignKey(Types)
    announce = models.TextField(blank=True, verbose_name=u'Краткое описание')
    description = models.TextFiled(blank=True, verbose_name=u'Описание', widget=CKEditorWidget())
    image = models.ImageField(width_field=100, verbose_name=u'Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_nameu'Цена')
    area = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=u'Площадь')
    active = models.BooleanField(verbose_name=u'Опубликован')

    def __unicode__(self):
	return self.name

    class Meta:
	verbose_name = u'Товары'
