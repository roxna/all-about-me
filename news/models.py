from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class SocialSource(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class NewsSource(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    # Mandatory
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    web_url = models.URLField()
    # Optional
    identifier = models.IntegerField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    source = models.ForeignKey(NewsSource, related_name='articles')

    def __unicode__(self):
        return self.title


class EntertainmentSource(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Entertainment(models.Model):
    # Mandatory
    title = models.CharField(max_length=200)
    url = models.URLField()
    # Optional
    description = models.TextField()
    identifier = models.IntegerField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)

    source = models.ForeignKey(EntertainmentSource, related_name='entertainment')

    def __unicode__(self):
        return self.title


class Person(AbstractUser):
    name = models.CharField(max_length=30)
    twitter_id = models.CharField(max_length=30, null=True)

    # Websites they follow
    news_preferences = models.ManyToManyField(NewsSource, related_name='followers', null=True, blank=True)
    social_preferences = models.ManyToManyField(SocialSource, related_name='followers', null=True, blank=True)
    entertainment_preferences = models.ManyToManyField(EntertainmentSource, related_name='followers', null=True, blank=True)

    # Favorites
    news_favorites = models.ManyToManyField(Article, related_name="followers", null=True)
    entertainment_favorites = models.ManyToManyField(Entertainment, related_name="followers", null=True)

    def __unicode__(self):
        return self.username
