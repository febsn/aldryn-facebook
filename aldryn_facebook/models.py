# -*- coding: utf-8 -*-
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

from aldryn_facebook.fields import LayoutStyleField, RefField, VerbField


class FacebookLikePlugin(CMSPlugin):

    href = models.URLField(_('URL to like'), blank=True, help_text=_('Defaults to page URL'))
    send = models.BooleanField(_('Send button'), default=True, help_text=_('Include a "Send" button.'))
    show_faces = models.BooleanField(_('Show Faces'), default=True,
                                     help_text=_('Show profile pictures when two or more friends like it.'))
    width = models.PositiveIntegerField(_('Width'), default=450)
    layout_style = LayoutStyleField()
    verb = VerbField()
    ref = RefField()


class FacebookSendPlugin(CMSPlugin):

    href = models.URLField(_('URL to send'), blank=True, help_text=_('Defaults to page URL.'))
    ref = RefField()


class FacebookFollowPlugin(CMSPlugin):

    href = models.URLField(_('Profile URL'), help_text=_('Facebook profile URL of the user to follow.'))
    show_faces = models.BooleanField(_('Show Faces'), default=True,
                                     help_text=_('Show profile pictures when two or more friends like it.'))
    width = models.PositiveIntegerField(_('Width'), default=450)
    layout_style = LayoutStyleField()


class FacebookCommentsPlugin(CMSPlugin):

    ORDERING = [
        ('social', _('Social ranking')),
        ('time', _('Chronological')),
        ('reverse_time', _('Reverse Chronological')),
    ]

    href = models.URLField(_('Discussion URL'), help_text=_('News feed stories on Facebook will link to this URL.'))
    width = models.PositiveIntegerField(_('Width'), default=450)
    num_posts = models.PositiveIntegerField(_('Posts'), default=10, help_text=_('How many posts to display.'))
    order_by = models.CharField(_('Ordering'), max_length=15, choices=ORDERING, default=ORDERING[0][0])


class FacebookActivityFeedPlugin(CMSPlugin):

    site = models.URLField(_('Domain'), blank=True,
                           help_text=_('Defaults to page domain. Domain to show activities for.'))
    action = models.CharField(_('Actions'), blank=True, max_length=200,
                              help_text=_('Comma separated list of actions to show activities for.'))
    width = models.PositiveIntegerField(_('Width'), default=300)
    height = models.PositiveIntegerField(_('Height'), blank=True, null=True)
    show_header = models.BooleanField(_('Display Header'), default=True)
    show_recommendations = models.BooleanField(_('Show Recommendations'), default=False)
    ref = RefField()


class FacebookRecommendationBoxPlugin(CMSPlugin):

    site = models.URLField(_('Domain'), blank=True,
                           help_text=_('Defaults to page domain. Domain to show activities for.'))
    action = models.CharField(_('Actions'), blank=True, max_length=200,
                              help_text=_('Comma separated list of actions to show activities for.'))
    width = models.PositiveIntegerField(_('Width'), default=300)
    height = models.PositiveIntegerField(_('Height'), blank=True, null=True)
    show_header = models.BooleanField(_('Display Header'), default=True)
    ref = RefField()


class FacebookRecommendationBarPlugin(CMSPlugin):

    TRIGGERS = [
        ('onvisible', _('When this plugin is visible in the browser')),
        ('25%', _('After 25% of content')),
        ('50%', _('After 50% of content')),
        ('75%', _('After 75% of content')),
        ('99%', _('After 99% of content')),
    ]

    SIDES = [
        ('right', _('Right')),
        ('left', _('Left')),
    ]

    href = models.URLField(_('Article URL'), blank=True,
                           help_text=_('Defaults to page URL. News feed stories on Facebook will link to this URL.'))
    trigger = models.CharField(_('Trigger'), max_length=10, choices=TRIGGERS, default=TRIGGERS[0][0],
                               help_text=_('When to show recommendation bar.'))
    read_time = models.PositiveIntegerField(_('Read Time'),
                                            validators=[MinValueValidator(10)],
                                            default=30,
                                            help_text=_('The number of seconds before the plugin will expand.'))
    verb = VerbField()
    side = models.CharField(_('Side'), max_length=10, choices=SIDES, default=SIDES[0][0])
    site = models.URLField(_('Domain'), blank=True,
                           help_text=_('Comma separated domain names to show the recommendations for. '
                                       'Defaults to page domain.'))
    num_recommendations = models.PositiveIntegerField(_('Recommendations'),
                                                      default=2,
                                                      help_text=_('How many recommendations to display.'),
                                                      validators=[MaxValueValidator(5)])
    ref = RefField()


class FacebookLikeBoxPlugin(CMSPlugin):

    href = models.URLField(_('Facebook Page URL'))
    width = models.PositiveIntegerField(_('Width'), default=300)
    height = models.PositiveIntegerField(_('Height'), blank=True, null=True)
    show_faces = models.BooleanField(_('Show Faces'), default=True)
    show_stream = models.BooleanField(_('Show Stream'), default=True)
    show_header = models.BooleanField(_('Display Header'), default=True)
    show_border = models.BooleanField(_('Display Border'), default=True)
    force_wall = models.BooleanField(_('Force Wall'), default=False, help_text=_('Force wall entries.'))


class FacebookFacepilePlugin(CMSPlugin):

    SIZES = [
        ('small', _('Small')),
        ('medium', _('Medium')),
        ('large', _('Large')),
    ]

    href = models.URLField(_('Facebook Page URL'),
                           help_text=_('Plugin will display people who have liked this page.'))
    action = models.CharField(_('Actions'), blank=True, max_length=200,
                              help_text=_('Limit displayed friends to engaged via one of the above actions.'))
    width = models.PositiveIntegerField(_('Width'), default=300)
    num_rows = models.PositiveIntegerField(_('Rows'), default=1, help_text=_('Maximum number of rows to display.'))
    size = models.CharField(_('Size'), max_length=6, choices=SIZES, default=SIZES[1][0],
                            help_text=_('Determines the size of the images and social context in the facepile.'))
    show_count = models.BooleanField(_('Show Count'), default=True)


class FacebookPagePlugin(CMSPlugin):
    href = models.URLField(_('Facebook Page URL'))
    width = models.PositiveIntegerField(
        _('Width'),
        blank=True,
        null=True,
        help_text=_('The pixel width of the plugin. Min. is 280 & Max. is 500')
    )
    height = models.PositiveIntegerField(
        _('Height'),
        blank=True,
        null=True,
        help_text=_('The maximum pixel height of the plugin. Min. is 130')
    )
    adapt_width = models.BooleanField(
        _('Adapt to plugin container width'),
        default=True,
        help_text=_('Plugin will try to fit inside the container')
    )
    hide_cover = models.BooleanField(
        _('Hide Cover'),
        default=False,
        help_text=_('Hide the cover photo in the header')
    )
    use_small_header = models.BooleanField(
        _('Use small header'),
        default=False,
        help_text=_('Use a smaller version of the page header')
    )
    show_facepile = models.BooleanField(
        _('Show friends\' faces'),
        default=True,
        help_text=_('Show profile photos when friends like this')
    )
    show_posts = models.BooleanField(
        _('Show Page posts'),
        default=False,
        help_text=_('Show posts from the Page\'s timeline')
    )
