# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_facebook', '0002_facebookpageplugin'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookpageplugin',
            name='adapt_width',
            field=models.BooleanField(default=True, help_text='Plugin will try to fit inside the container', verbose_name='Adapt to plugin container width'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='facebookpageplugin',
            name='use_small_header',
            field=models.BooleanField(default=False, help_text='Use a smaller version of the page header', verbose_name='Use small header'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='facebookpageplugin',
            name='hide_cover',
            field=models.BooleanField(default=False, help_text='Hide the cover photo in the header', verbose_name='Hide Cover'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='facebookpageplugin',
            name='show_facepile',
            field=models.BooleanField(default=True, help_text='Show profile photos when friends like this', verbose_name="Show friends' faces"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='facebookpageplugin',
            name='show_posts',
            field=models.BooleanField(default=False, help_text="Show posts from the Page's timeline", verbose_name='Show Page posts'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='facebookpageplugin',
            name='width',
            field=models.PositiveIntegerField(help_text='The pixel width of the plugin. Min. is 280 & Max. is 500', null=True, verbose_name='Width', blank=True),
            preserve_default=True,
        ),
    ]
