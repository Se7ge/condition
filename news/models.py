# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime, timedelta

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок новости', blank=False, null=False)
    brief = models.TextField(verbose_name=u'Анонс', blank=True)
    description = RichTextField(verbose_name=u'Содержание новости', blank=False)
    created = models.DateTimeField(u'Дата создания', auto_now=False,
                              auto_now_add=True, blank=True,
                              default=datetime.now)
    img = models.ImageField(upload_to='images/news/', blank=True, null=True, verbose_name=u'Изображение')
    active = models.BooleanField(verbose_name=u'Опубликована', blank=True)

    class Meta:
	verbose_name = u'Новость'
	verbose_name_plural = u'Новости'
	ordering = ('-created',)

    def __unicode__(self):
	return self.title

