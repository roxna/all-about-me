# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsSource'
        db.create_table(u'news_newssource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'news', ['NewsSource'])

        # Adding model 'Entertainment'
        db.create_table(u'news_entertainment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('identifier', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('published_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entertainment', to=orm['news.EntertainmentSource'])),
        ))
        db.send_create_signal(u'news', ['Entertainment'])

        # Adding model 'Person'
        db.create_table(u'news_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('twitter_id', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
        ))
        db.send_create_signal(u'news', ['Person'])

        # Adding M2M table for field groups on 'Person'
        m2m_table_name = db.shorten_name(u'news_person_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'news.person'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'Person'
        m2m_table_name = db.shorten_name(u'news_person_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'news.person'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'permission_id'])

        # Adding M2M table for field news_preferences on 'Person'
        m2m_table_name = db.shorten_name(u'news_person_news_preferences')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'news.person'], null=False)),
            ('newssource', models.ForeignKey(orm[u'news.newssource'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'newssource_id'])

        # Adding M2M table for field social_preferences on 'Person'
        m2m_table_name = db.shorten_name(u'news_person_social_preferences')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'news.person'], null=False)),
            ('socialsource', models.ForeignKey(orm[u'news.socialsource'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'socialsource_id'])

        # Adding M2M table for field entertainment_preferences on 'Person'
        m2m_table_name = db.shorten_name(u'news_person_entertainment_preferences')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'news.person'], null=False)),
            ('entertainmentsource', models.ForeignKey(orm[u'news.entertainmentsource'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'entertainmentsource_id'])

        # Adding M2M table for field news_favorites on 'Person'
        m2m_table_name = db.shorten_name(u'news_person_news_favorites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'news.person'], null=False)),
            ('article', models.ForeignKey(orm[u'news.article'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'article_id'])

        # Adding model 'Article'
        db.create_table(u'news_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('abstract', self.gf('django.db.models.fields.TextField')()),
            ('web_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('identifier', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('published_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles', to=orm['news.NewsSource'])),
        ))
        db.send_create_signal(u'news', ['Article'])

        # Adding model 'SocialSource'
        db.create_table(u'news_socialsource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'news', ['SocialSource'])

        # Adding model 'EntertainmentSource'
        db.create_table(u'news_entertainmentsource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'news', ['EntertainmentSource'])


    def backwards(self, orm):
        # Deleting model 'NewsSource'
        db.delete_table(u'news_newssource')

        # Deleting model 'Entertainment'
        db.delete_table(u'news_entertainment')

        # Deleting model 'Person'
        db.delete_table(u'news_person')

        # Removing M2M table for field groups on 'Person'
        db.delete_table(db.shorten_name(u'news_person_groups'))

        # Removing M2M table for field user_permissions on 'Person'
        db.delete_table(db.shorten_name(u'news_person_user_permissions'))

        # Removing M2M table for field news_preferences on 'Person'
        db.delete_table(db.shorten_name(u'news_person_news_preferences'))

        # Removing M2M table for field social_preferences on 'Person'
        db.delete_table(db.shorten_name(u'news_person_social_preferences'))

        # Removing M2M table for field entertainment_preferences on 'Person'
        db.delete_table(db.shorten_name(u'news_person_entertainment_preferences'))

        # Removing M2M table for field news_favorites on 'Person'
        db.delete_table(db.shorten_name(u'news_person_news_favorites'))

        # Deleting model 'Article'
        db.delete_table(u'news_article')

        # Deleting model 'SocialSource'
        db.delete_table(u'news_socialsource')

        # Deleting model 'EntertainmentSource'
        db.delete_table(u'news_entertainmentsource')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'news.article': {
            'Meta': {'object_name': 'Article'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'author': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'published_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles'", 'to': u"orm['news.NewsSource']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'web_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'news.entertainment': {
            'Meta': {'object_name': 'Entertainment'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'published_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entertainment'", 'to': u"orm['news.EntertainmentSource']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'news.entertainmentsource': {
            'Meta': {'object_name': 'EntertainmentSource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'news.newssource': {
            'Meta': {'object_name': 'NewsSource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'news.person': {
            'Meta': {'object_name': 'Person'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'entertainment_preferences': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'followers'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['news.EntertainmentSource']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'news_favorites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'followers'", 'null': 'True', 'to': u"orm['news.Article']"}),
            'news_preferences': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'followers'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['news.NewsSource']"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'social_preferences': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'followers'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['news.SocialSource']"}),
            'twitter_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'news.socialsource': {
            'Meta': {'object_name': 'SocialSource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['news']