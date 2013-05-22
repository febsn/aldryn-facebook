# -*- coding: utf-8 -*-
from cmscloud_client import forms


class Form(forms.BaseForm):

    COLOR_SCHEMES = [
        ('light', 'Light'),
        ('dark', 'Dark'),
    ]

    FONTS = [
        ('arial', 'Arial'),
        ('lucida grande', 'Lucida Grande'),
        ('segoe ui', 'Segoe UI'),
        ('tahoma', 'Tahoma'),
        ('trebuchet ms', 'Trebuchet MS'),
        ('verdana', 'Verdana'),
    ]

    app_id = forms.CharField('Facebook App ID', required=False)
    color_scheme = forms.SelectField('Color Scheme', choices=COLOR_SCHEMES)
    font = forms.SelectField('Font', choices=FONTS, required=False)

    def to_settings(self, data, settings):
        settings['FACEBOOK_APP_ID'] = data['app_id']
        settings['FACEBOOK_COLOR_SCHEME'] = data['color_scheme']
        settings['FACEBOOK_FONT'] = data['font']
        return settings
