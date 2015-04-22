# -*- coding: utf-8 -*-
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class RefField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = _('Ref Label')
        kwargs['blank'] = True
        kwargs['max_length'] = 50
        kwargs['help_text'] = _('A label for tracking referrals.')
        kwargs['validators'] = [RegexValidator(regex=r'^[a-z+/=.:_-]*$')]
        super(RefField, self).__init__(*args, **kwargs)
            

    def south_field_triple(self):
        from south.modelsinspector import introspector
        field_class = "django.db.models.CharField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)


class LayoutStyleField(models.CharField):

    LAYOUTS = [
        ('standard', _('Standard')),
        ('button_count', _('Button Count')),
        ('box_count', _('Box Count')),
    ]

    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = _('Layout Style')
        kwargs['max_length'] = 20
        kwargs['choices'] = self.LAYOUTS
        kwargs['default'] = self.LAYOUTS[0][0]
        super(LayoutStyleField, self).__init__(*args, **kwargs)

    def south_field_triple(self):
        from south.modelsinspector import introspector
        field_class = "django.db.models.CharField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)


class VerbField(models.CharField):

    VERBS = [
        ('like', _('Like')),
        ('recommend', _('Recommend')),
    ]

    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = _('Verb to display')
        kwargs['max_length'] = 10
        kwargs['choices'] = self.VERBS
        kwargs['default'] = self.VERBS[0][0]
        super(VerbField, self).__init__(*args, **kwargs)

    def south_field_triple(self):
        from south.modelsinspector import introspector
        field_class = "django.db.models.CharField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)
