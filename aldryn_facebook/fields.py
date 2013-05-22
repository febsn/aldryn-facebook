# -*- coding: utf-8 -*-
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class RefField(models.CharField):

    def __init__(self):
        super(RefField, self).__init__(
            _('Ref Label'),
            blank=True,
            max_length=50,
            help_text=_('A label for tracking referrals.'),
            validators=[RegexValidator(regex=r'^[a-z+/=.:_-]*$')])

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

    def __init__(self):
        super(LayoutStyleField, self).__init__(
            _('Layout Style'),
            max_length=20,
            choices=self.LAYOUTS,
            default=self.LAYOUTS[0][0])

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

    def __init__(self):
        super(VerbField, self).__init__(
            _('Verb to display'),
            max_length=10,
            choices=self.VERBS,
            default=self.VERBS[0][0])

    def south_field_triple(self):
        from south.modelsinspector import introspector
        field_class = "django.db.models.CharField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)
