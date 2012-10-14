# -*- coding: utf-8 -*-
from django.db import models
from django.db import utils

import datetime
from ckeditor.widgets import CKEditorWidget

class Services(models.Model):
   name = models.CharField(max_length=50, blank=False, verbose_name=u'Название')
   description = models.TextField(blank=True, null=True, verbose_name=u'Описание')
   ordernum = models.IntegerField(blank=True, default=0, verbose_name=u'Порядок вывода')

   def __unicode__(self):
       return self.name

   class Meta:
       ordering = ["ordernum"]
       verbose_name = u'Услуга'
       verbose_name_plural = u'Услуги'

