#-*- coding: utf-8 -*-
from django.db import models
from django.db import utils

import datetime
from ckeditor.widgets import CKEditorWidget

class Types(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name=u'Название')
    description = models.TextField(blank=True, null=True, verbose_name=u'Описание')
    
    def __unicode__(self):
	return self.name
    
    class Meta:
        ordering = ["name"]
	verbose_name = u'Тип'
	verbose_name_plural = u'Типы'

class Producers(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name=u'Производитель')
    description = models.TextField(blank=True, null=True, verbose_name=u'Описание')

    def __unicode__(self):
	return self.name

    class Meta:
	ordering = ["name"]
	verbose_name = u'Производитель'
	verbose_name_plural = u'Производители'

class Products(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name=u'Название')
    producer_id = models.ForeignKey(Producers, verbose_name=u'Производитель')
    type_id = models.ForeignKey(Types, verbose_name=u'Тип')
    announce = models.TextField(blank=True, null=True, verbose_name=u'Краткое описание')
    description = models.TextField(blank=True, null=True, verbose_name=u'Описание')
    image = models.ImageField(upload_to='images/catalog/', blank=True, verbose_name=u'Изображение')
    price = models.DecimalField(max_digits=10,blank=True, null=True, decimal_places=2, verbose_name=u'Цена')
    area = models.DecimalField(max_digits=5, blank=True, null=True, decimal_places=2, verbose_name=u'Площадь')
    active = models.BooleanField(verbose_name=u'Опубликован', blank=True)

    def __unicode__(self):
	return self.name

    class Meta:
	verbose_name = u'Товар'
	verbose_name_plural = u'Товары'
