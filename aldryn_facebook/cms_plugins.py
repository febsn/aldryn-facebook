# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import get_language, ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
import locale

from aldryn_facebook import models


class FacebookPluginBase(CMSPluginBase):

    module = 'Facebook'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['long_language_code'] = locale.normalize(get_language()).split('.')[0]
        context['facebook_app_id'] = getattr(settings, 'FACEBOOK_APP_ID', None)
        context['facebook_color_scheme'] = getattr(settings, 'FACEBOOK_COLOR_SCHEME', None)
        context['facebook_font'] = getattr(settings, 'FACEBOOK_FONT', None)
        return context


class FacebookLikePlugin(FacebookPluginBase):

    render_template = 'aldryn_facebook/like.html'
    name = _('Like')
    model = models.FacebookLikePlugin

plugin_pool.register_plugin(FacebookLikePlugin)


class FacebookSendPlugin(FacebookPluginBase):

    render_template = 'aldryn_facebook/send.html'
    name = _('Send')
    model = models.FacebookSendPlugin

plugin_pool.register_plugin(FacebookSendPlugin)


class FacebookFollowPlugin(FacebookPluginBase):

    render_template = 'aldryn_facebook/follow.html'
    name = _('Follow')
    model = models.FacebookFollowPlugin

plugin_pool.register_plugin(FacebookFollowPlugin)


class FacebookCommentsPlugin(FacebookPluginBase):

    render_template = 'aldryn_facebook/comments.html'
    name = _('Comments')
    model = models.FacebookCommentsPlugin

plugin_pool.register_plugin(FacebookCommentsPlugin)


class FacebookActivityFeedPlugin(FacebookPluginBase):

    render_template = 'aldryn_facebook/activity_feed.html'
    name = _('Activity Feed')
    model = models.FacebookActivityFeedPlugin

plugin_pool.register_plugin(FacebookActivityFeedPlugin)


class FacebookRecommendationBoxPlugin(FacebookPluginBase):

    render_template = 'aldryn_facebook/recommendation_box.html'
    name = _('Recommendation Box')
    model = models.FacebookRecommendationBoxPlugin

plugin_pool.register_plugin(FacebookRecommendationBoxPlugin)


class FacebookRecommendationBarPlugin(FacebookPluginBase):

    render_template = 'aldryn_facebook/recommendation_bar.html'
    name = _('Recommendation Bar')
    model = models.FacebookRecommendationBarPlugin

plugin_pool.register_plugin(FacebookRecommendationBarPlugin)


class FacebookLikeBoxPlugin(FacebookPluginBase):

    render_template = 'aldryn_facebook/like_box.html'
    name = _('Like Box')
    model = models.FacebookLikeBoxPlugin

plugin_pool.register_plugin(FacebookLikeBoxPlugin)


class FacebookFacepilePlugin(FacebookPluginBase):

    render_template = 'aldryn_facebook/facepile.html'
    name = _('Facepile')
    model = models.FacebookFacepilePlugin

plugin_pool.register_plugin(FacebookFacepilePlugin)
