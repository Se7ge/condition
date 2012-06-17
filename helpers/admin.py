#-*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from ckeditor.widgets import CKEditorWidget
 
class CkeditorFlatpageForm(FlatpageForm):
    content = forms.CharField(widget=CKEditorWidget())
    
class CkeditorFlatPageAdmin(FlatPageAdmin):
    form = CkeditorFlatpageForm
    
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CkeditorFlatPageAdmin)

#from django.contrib import admin
#from django.contrib.flatpages.models import FlatPage

## Note: we are renaming the original Admin and Form as we import them
#from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
#from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
#
#from django import forms
#from ckeditor.widgets import CKEditorWidget
#
#class FlatpageForm(FlatpageFormOld):
#    content = forms.CharField(widget=CKEditorWidget())
#    class Meta:
#        model = FlatPage # this is not automatically inherited from FlatpageFormOld

#
#class FlatPageAdmin(FlatPageAdminOld):
#    form = FlatpageForm
#
#
## We have to unregister the normal admin, and then reregister ours
#admin.site.unregister(FlatPage)
#admin.site.register(FlatPage, FlatPageAdmin)
