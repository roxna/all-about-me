from django.contrib import admin
from news.models import *

# Register your models here.


class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ['name']


class SocialAdmin(admin.ModelAdmin):
    list_display = ['name']


class PersonAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'abstract', 'published_date', 'web_url']


admin.site.register(NewsSource, NewsSourceAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Article, ArticleAdmin)