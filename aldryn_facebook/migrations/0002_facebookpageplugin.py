# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('aldryn_facebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookPagePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('href', models.URLField(verbose_name='Facebook Page URL')),
                ('width', models.PositiveIntegerField(default=340, help_text='The pixel width of the plugin. Min. is 280 & Max. is 500', verbose_name='Width')),
                ('height', models.PositiveIntegerField(help_text='The maximum pixel height of the plugin. Min. is 130', null=True, verbose_name='Height', blank=True)),
                ('hide_cover', models.BooleanField(default=False, help_text='Hide cover photo in the header', verbose_name='Hide Cover')),
                ('show_facepile', models.BooleanField(default=True, help_text='Show profile photos when friends like this', verbose_name='Show Facepile')),
                ('show_posts', models.BooleanField(default=False, help_text="Show posts from the Page's timeline", verbose_name='Show Posts')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
