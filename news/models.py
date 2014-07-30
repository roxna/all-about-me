from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Social(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class NewsSource(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Entertainment(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Person(AbstractUser):
    name = models.CharField(max_length=30)
    news_preferences = models.ManyToManyField(NewsSource, related_name='followers', null=True, blank=True)
    social_preferences = models.ManyToManyField(Social, related_name='followers', null=True, blank=True)
    entertainment_preferences = models.ManyToManyField(Entertainment, related_name='followers', null=True, blank=True)
    twitter_id = models.CharField(max_length=30)

    def __unicode__(self):
        return self.username


class Article(models.Model):
    identifier = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    author = models.TextField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    web_url = models.URLField()
    image_url = models.URLField(blank=True, null=True)
    source = models.ForeignKey(NewsSource, related_name='articles')

    def __unicode__(self):
        return self.headline


# Can add "Keyword/Tag" model for search