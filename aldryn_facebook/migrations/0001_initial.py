# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import aldryn_facebook.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookActivityFeedPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('site', models.URLField(help_text='Defaults to page domain. Domain to show activities for.', verbose_name='Domain', blank=True)),
                ('action', models.CharField(help_text='Comma separated list of actions to show activities for.', max_length=200, verbose_name='Actions', blank=True)),
                ('width', models.PositiveIntegerField(default=300, verbose_name='Width')),
                ('height', models.PositiveIntegerField(null=True, verbose_name='Height', blank=True)),
                ('show_header', models.BooleanField(default=True, verbose_name='Display Header')),
                ('show_recommendations', models.BooleanField(default=False, verbose_name='Show Recommendations')),
                ('ref', aldryn_facebook.fields.RefField(blank=True, help_text='A label for tracking referrals.', max_length=50, verbose_name='Ref Label', validators=[django.core.validators.RegexValidator(regex=b'^[a-z+/=.:_-]*$')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FacebookCommentsPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('href', models.URLField(help_text='News feed stories on Facebook will link to this URL.', verbose_name='Discussion URL')),
                ('width', models.PositiveIntegerField(default=450, verbose_name='Width')),
                ('num_posts', models.PositiveIntegerField(default=10, help_text='How many posts to display.', verbose_name='Posts')),
                ('order_by', models.CharField(default=b'social', max_length=15, verbose_name='Ordering', choices=[(b'social', 'Social ranking'), (b'time', 'Chronological'), (b'reverse_time', 'Reverse Chronological')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FacebookFacepilePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('href', models.URLField(help_text='Plugin will display people who have liked this page.', verbose_name='Facebook Page URL')),
                ('action', models.CharField(help_text='Limit displayed friends to engaged via one of the above actions.', max_length=200, verbose_name='Actions', blank=True)),
                ('width', models.PositiveIntegerField(default=300, verbose_name='Width')),
                ('num_rows', models.PositiveIntegerField(default=1, help_text='Maximum number of rows to display.', verbose_name='Rows')),
                ('size', models.CharField(default=b'medium', help_text='Determines the size of the images and social context in the facepile.', max_length=6, verbose_name='Size', choices=[(b'small', 'Small'), (b'medium', 'Medium'), (b'large', 'Large')])),
                ('show_count', models.BooleanField(default=True, verbose_name='Show Count')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FacebookFollowPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('href', models.URLField(help_text='Facebook profile URL of the user to follow.', verbose_name='Profile URL')),
                ('show_faces', models.BooleanField(default=True, help_text='Show profile pictures when two or more friends like it.', verbose_name='Show Faces')),
                ('width', models.PositiveIntegerField(default=450, verbose_name='Width')),
                ('layout_style', aldryn_facebook.fields.LayoutStyleField(default=b'standard', max_length=20, verbose_name='Layout Style', choices=[(b'standard', 'Standard'), (b'button_count', 'Button Count'), (b'box_count', 'Box Count')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FacebookLikeBoxPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('href', models.URLField(verbose_name='Facebook Page URL')),
                ('width', models.PositiveIntegerField(default=300, verbose_name='Width')),
                ('height', models.PositiveIntegerField(null=True, verbose_name='Height', blank=True)),
                ('show_faces', models.BooleanField(default=True, verbose_name='Show Faces')),
                ('show_stream', models.BooleanField(default=True, verbose_name='Show Stream')),
                ('show_header', models.BooleanField(default=True, verbose_name='Display Header')),
                ('show_border', models.BooleanField(default=True, verbose_name='Display Border')),
                ('force_wall', models.BooleanField(default=False, help_text='Force wall entries.', verbose_name='Force Wall')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FacebookLikePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('href', models.URLField(help_text='Defaults to page URL', verbose_name='URL to like', blank=True)),
                ('send', models.BooleanField(default=True, help_text='Include a "Send" button.', verbose_name='Send button')),
                ('show_faces', models.BooleanField(default=True, help_text='Show profile pictures when two or more friends like it.', verbose_name='Show Faces')),
                ('width', models.PositiveIntegerField(default=450, verbose_name='Width')),
                ('layout_style', aldryn_facebook.fields.LayoutStyleField(default=b'standard', max_length=20, verbose_name='Layout Style', choices=[(b'standard', 'Standard'), (b'button_count', 'Button Count'), (b'box_count', 'Box Count')])),
                ('verb', aldryn_facebook.fields.VerbField(default=b'like', max_length=10, verbose_name='Verb to display', choices=[(b'like', 'Like'), (b'recommend', 'Recommend')])),
                ('ref', aldryn_facebook.fields.RefField(blank=True, help_text='A label for tracking referrals.', max_length=50, verbose_name='Ref Label', validators=[django.core.validators.RegexValidator(regex=b'^[a-z+/=.:_-]*$')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FacebookRecommendationBarPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('href', models.URLField(help_text='Defaults to page URL. News feed stories on Facebook will link to this URL.', verbose_name='Article URL', blank=True)),
                ('trigger', models.CharField(default=b'onvisible', help_text='When to show recommendation bar.', max_length=10, verbose_name='Trigger', choices=[(b'onvisible', 'When this plugin is visible in the browser'), (b'25%', 'After 25% of content'), (b'50%', 'After 50% of content'), (b'75%', 'After 75% of content'), (b'99%', 'After 99% of content')])),
                ('read_time', models.PositiveIntegerField(default=30, help_text='The number of seconds before the plugin will expand.', verbose_name='Read Time', validators=[django.core.validators.MinValueValidator(10)])),
                ('verb', aldryn_facebook.fields.VerbField(default=b'like', max_length=10, verbose_name='Verb to display', choices=[(b'like', 'Like'), (b'recommend', 'Recommend')])),
                ('side', models.CharField(default=b'right', max_length=10, verbose_name='Side', choices=[(b'right', 'Right'), (b'left', 'Left')])),
                ('site', models.URLField(help_text='Comma separated domain names to show the recommendations for. Defaults to page domain.', verbose_name='Domain', blank=True)),
                ('num_recommendations', models.PositiveIntegerField(default=2, help_text='How many recommendations to display.', verbose_name='Recommendations', validators=[django.core.validators.MaxValueValidator(5)])),
                ('ref', aldryn_facebook.fields.RefField(blank=True, help_text='A label for tracking referrals.', max_length=50, verbose_name='Ref Label', validators=[django.core.validators.RegexValidator(regex=b'^[a-z+/=.:_-]*$')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FacebookRecommendationBoxPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('site', models.URLField(help_text='Defaults to page domain. Domain to show activities for.', verbose_name='Domain', blank=True)),
                ('action', models.CharField(help_text='Comma separated list of actions to show activities for.', max_length=200, verbose_name='Actions', blank=True)),
                ('width', models.PositiveIntegerField(default=300, verbose_name='Width')),
                ('height', models.PositiveIntegerField(null=True, verbose_name='Height', blank=True)),
                ('show_header', models.BooleanField(default=True, verbose_name='Display Header')),
                ('ref', aldryn_facebook.fields.RefField(blank=True, help_text='A label for tracking referrals.', max_length=50, verbose_name='Ref Label', validators=[django.core.validators.RegexValidator(regex=b'^[a-z+/=.:_-]*$')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FacebookSendPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('href', models.URLField(help_text='Defaults to page URL.', verbose_name='URL to send', blank=True)),
                ('ref', aldryn_facebook.fields.RefField(blank=True, help_text='A label for tracking referrals.', max_length=50, verbose_name='Ref Label', validators=[django.core.validators.RegexValidator(regex=b'^[a-z+/=.:_-]*$')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
