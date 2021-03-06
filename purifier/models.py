#-*- coding: utf-8 -*-
from django.db import models
from django.db import utils

import datetime
from ckeditor.widgets import CKEditorWidget


class Purifier_Types(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name=u'Название')
    description = models.TextField(blank=True, null=True, verbose_name=u'Описание')
    ordernum = models.IntegerField(blank=True, default=0, verbose_name=u'Порядок вывода')
    image = models.ImageField(upload_to='images/purifier/', blank=True, verbose_name=u'Изображение', default="")
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["ordernum"]
        verbose_name = u'Тип увлажнителя/очистителя воздуха'
        verbose_name_plural = u'Типы увлажнителей/очистителей воздуха'


class Purifier_Producers(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name=u'Производитель')
    description = models.TextField(blank=True, null=True, verbose_name=u'Описание')
    image = models.ImageField(upload_to='images/purifier/', blank=True, verbose_name=u'Изображение', default="")
    ordernum = models.IntegerField(blank=True, default=0, verbose_name=u'Порядок вывода')
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["ordernum"]
        verbose_name = u'Производитель'
        verbose_name_plural = u'Производители'


class Purifier_Products(models.Model):
    name = models.CharField(max_length=250, blank=False, verbose_name=u'Название')
#    producer_id = models.ForeignKey(Producers, verbose_name=u'Производитель')
    type_id = models.ForeignKey(Purifier_Types, verbose_name=u'Тип')
    producer = models.ForeignKey(Purifier_Producers, verbose_name=u'Производитель')
    announce = models.TextField(blank=True, null=True, verbose_name=u'Краткое описание')
    description = models.TextField(blank=True, null=True, verbose_name=u'Описание')
    image = models.ImageField(upload_to='images/purifier/', blank=True, verbose_name=u'Изображение')
    price = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2, verbose_name=u'Цена')
    area = models.DecimalField(max_digits=5, blank=True, null=True, decimal_places=2, verbose_name=u'Площадь')
    active = models.BooleanField(verbose_name=u'Опубликован', blank=True)
#    show_in_main = models.BooleanField(verbose_name=u'Показывать на главной', blank=True, default=False)
    raiting = models.IntegerField(blank=True, default=0, verbose_name=u'Рейтинг товара')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Увлажнители и очистители воздуха'
        verbose_name_plural = u'Увлажнители и очистители воздуха'
