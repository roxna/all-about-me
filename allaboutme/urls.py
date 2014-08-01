from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'allaboutme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'news.views.home', name='home'),

    # PAGES
    url(r'^profile/$', 'news.views.profile', name='profile'),
    url(r'^preferences/$', 'news.views.preferences', name='preferences'),
    url(r'^favorites/$', 'news.views.favorites', name='favorites'),
    url(r'^dashboard/$', 'news.views.dashboard', name='dashboard'),
    url(r'^twitter/$', 'news.views.twitter', name='twitter'),

    # NON-PAGE URLS
    url(r'^add_favorite_news/$', 'news.views.add_favorite_news', name='add_favorite_news'),
    url(r'^remove_favorite_news/$', 'news.views.remove_favorite_news', name='remove_favorite_news'),
    url(r'^add_favorite_entertainment/$', 'news.views.add_favorite_entertainment', name='add_favorite_entertainment'),
    url(r'^remove_favorite_entertainment/$', 'news.views.remove_favorite_entertainment', name='remove_favorite_entertainment'),

    # LOGIN
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^social_logins/$', 'news.views.social_logins', name='social_logins'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

    # PACKAGES
    url(r'', include('social_auth.urls')),

)

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)