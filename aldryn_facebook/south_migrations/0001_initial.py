# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FacebookLikePlugin'
        db.create_table('cmsplugin_facebooklikeplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('send', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('show_faces', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(default=450)),
            ('layout_style', self.gf('django.db.models.CharField')(default='standard', max_length=20)),
            ('verb', self.gf('django.db.models.CharField')(default='like', max_length=10)),
            ('ref', self.gf('django.db.models.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('aldryn_facebook', ['FacebookLikePlugin'])

        # Adding model 'FacebookSendPlugin'
        db.create_table('cmsplugin_facebooksendplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('ref', self.gf('django.db.models.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('aldryn_facebook', ['FacebookSendPlugin'])

        # Adding model 'FacebookFollowPlugin'
        db.create_table('cmsplugin_facebookfollowplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('show_faces', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(default=450)),
            ('layout_style', self.gf('django.db.models.CharField')(default='standard', max_length=20)),
        ))
        db.send_create_signal('aldryn_facebook', ['FacebookFollowPlugin'])

        # Adding model 'FacebookCommentsPlugin'
        db.create_table('cmsplugin_facebookcommentsplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(default=450)),
            ('num_posts', self.gf('django.db.models.fields.PositiveIntegerField')(default=10)),
            ('order_by', self.gf('django.db.models.fields.CharField')(default='social', max_length=15)),
        ))
        db.send_create_signal('aldryn_facebook', ['FacebookCommentsPlugin'])

        # Adding model 'FacebookActivityFeedPlugin'
        db.create_table('cmsplugin_facebookactivityfeedplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(default=300)),
            ('height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('show_header', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('show_recommendations', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ref', self.gf('django.db.models.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('aldryn_facebook', ['FacebookActivityFeedPlugin'])

        # Adding model 'FacebookRecommendationBoxPlugin'
        db.create_table('cmsplugin_facebookrecommendationboxplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(default=300)),
            ('height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('show_header', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('ref', self.gf('django.db.models.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('aldryn_facebook', ['FacebookRecommendationBoxPlugin'])

        # Adding model 'FacebookRecommendationBarPlugin'
        db.create_table('cmsplugin_facebookrecommendationbarplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('trigger', self.gf('django.db.models.fields.CharField')(default='onvisible', max_length=10)),
            ('read_time', self.gf('django.db.models.fields.PositiveIntegerField')(default=30)),
            ('verb', self.gf('django.db.models.CharField')(default='like', max_length=10)),
            ('side', self.gf('django.db.models.fields.CharField')(default='right', max_length=10)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('ref', self.gf('django.db.models.CharField')(max_length=50, blank=True)),
            ('num_recommendations', self.gf('django.db.models.fields.PositiveIntegerField')(default=2)),
        ))
        db.send_create_signal('aldryn_facebook', ['FacebookRecommendationBarPlugin'])

        # Adding model 'FacebookLikeBoxPlugin'
        db.create_table('cmsplugin_facebooklikeboxplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(default=300)),
            ('height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('show_faces', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('show_stream', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('show_header', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('show_border', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('force_wall', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('aldryn_facebook', ['FacebookLikeBoxPlugin'])

        # Adding model 'FacebookFacepilePlugin'
        db.create_table('cmsplugin_facebookfacepileplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(default=300)),
            ('num_rows', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('size', self.gf('django.db.models.fields.CharField')(default='medium', max_length=6)),
            ('show_count', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('aldryn_facebook', ['FacebookFacepilePlugin'])


    def backwards(self, orm):
        # Deleting model 'FacebookLikePlugin'
        db.delete_table('cmsplugin_facebooklikeplugin')

        # Deleting model 'FacebookSendPlugin'
        db.delete_table('cmsplugin_facebooksendplugin')

        # Deleting model 'FacebookFollowPlugin'
        db.delete_table('cmsplugin_facebookfollowplugin')

        # Deleting model 'FacebookCommentsPlugin'
        db.delete_table('cmsplugin_facebookcommentsplugin')

        # Deleting model 'FacebookActivityFeedPlugin'
        db.delete_table('cmsplugin_facebookactivityfeedplugin')

        # Deleting model 'FacebookRecommendationBoxPlugin'
        db.delete_table('cmsplugin_facebookrecommendationboxplugin')

        # Deleting model 'FacebookRecommendationBarPlugin'
        db.delete_table('cmsplugin_facebookrecommendationbarplugin')

        # Deleting model 'FacebookLikeBoxPlugin'
        db.delete_table('cmsplugin_facebooklikeboxplugin')

        # Deleting model 'FacebookFacepilePlugin'
        db.delete_table('cmsplugin_facebookfacepileplugin')


    models = {
        'aldryn_facebook.facebookactivityfeedplugin': {
            'Meta': {'object_name': 'FacebookActivityFeedPlugin', 'db_table': "'cmsplugin_facebookactivityfeedplugin'", '_ormbases': ['cms.CMSPlugin']},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'show_header': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_recommendations': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '300'})
        },
        'aldryn_facebook.facebookcommentsplugin': {
            'Meta': {'object_name': 'FacebookCommentsPlugin', 'db_table': "'cmsplugin_facebookcommentsplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'num_posts': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'order_by': ('django.db.models.fields.CharField', [], {'default': "'social'", 'max_length': '15'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '450'})
        },
        'aldryn_facebook.facebookfacepileplugin': {
            'Meta': {'object_name': 'FacebookFacepilePlugin', 'db_table': "'cmsplugin_facebookfacepileplugin'", '_ormbases': ['cms.CMSPlugin']},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'num_rows': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'show_count': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'default': "'medium'", 'max_length': '6'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '300'})
        },
        'aldryn_facebook.facebookfollowplugin': {
            'Meta': {'object_name': 'FacebookFollowPlugin', 'db_table': "'cmsplugin_facebookfollowplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'layout_style': ('django.db.models.CharField', [], {'default': "'standard'", 'max_length': '20'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '450'})
        },
        'aldryn_facebook.facebooklikeboxplugin': {
            'Meta': {'object_name': 'FacebookLikeBoxPlugin', 'db_table': "'cmsplugin_facebooklikeboxplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'force_wall': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'show_border': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_header': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_stream': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '300'})
        },
        'aldryn_facebook.facebooklikeplugin': {
            'Meta': {'object_name': 'FacebookLikePlugin', 'db_table': "'cmsplugin_facebooklikeplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'layout_style': ('django.db.models.CharField', [], {'default': "'standard'", 'max_length': '20'}),
            'ref': ('django.db.models.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'send': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'verb': ('django.db.models.CharField', [], {'default': "'like'", 'max_length': '10'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '450'})
        },
        'aldryn_facebook.facebookrecommendationbarplugin': {
            'Meta': {'object_name': 'FacebookRecommendationBarPlugin', 'db_table': "'cmsplugin_facebookrecommendationbarplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'num_recommendations': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2'}),
            'read_time': ('django.db.models.fields.PositiveIntegerField', [], {'default': '30'}),
            'ref': ('django.db.models.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'side': ('django.db.models.fields.CharField', [], {'default': "'right'", 'max_length': '10'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'trigger': ('django.db.models.fields.CharField', [], {'default': "'onvisible'", 'max_length': '10'}),
            'verb': ('django.db.models.CharField', [], {'default': "'like'", 'max_length': '10'})
        },
        'aldryn_facebook.facebookrecommendationboxplugin': {
            'Meta': {'object_name': 'FacebookRecommendationBoxPlugin', 'db_table': "'cmsplugin_facebookrecommendationboxplugin'", '_ormbases': ['cms.CMSPlugin']},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'show_header': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '300'})
        },
        'aldryn_facebook.facebooksendplugin': {
            'Meta': {'object_name': 'FacebookSendPlugin', 'db_table': "'cmsplugin_facebooksendplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'ref': ('django.db.models.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['aldryn_facebook']