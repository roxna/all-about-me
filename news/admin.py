from django.contrib import admin
from news.models import *

# Register your models here.

# Social sources and tweets etc.
class SocialSourceAdmin(admin.ModelAdmin):
    list_display = ['name']


# News sources and articles
class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ['name']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'abstract', 'web_url']


# Entertainment sources and videos etc.
class EntertainmentSourceAdmin(admin.ModelAdmin):
    list_display = ['name']


class EntertainmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


# User
class PersonAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']



admin.site.register(NewsSource, NewsSourceAdmin)
admin.site.register(SocialSource, SocialSourceAdmin)
admin.site.register(EntertainmentSource, EntertainmentSourceAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Entertainment, EntertainmentAdmin)
