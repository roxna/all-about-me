import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from allaboutme.settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_SECRET, \
    TWITTER_ACCESS_TOKEN
from news.forms import RegistrationForm, PreferencesForm, ProfileForm
from news.models import *
import tweepy

# Create your views here.


def home(request):
    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return redirect("/preferences/")

    register_form = RegistrationForm()
    return render(request, 'home.html', {'register_form': register_form})


@login_required
def dashboard(request):
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)

    if request.user.twitter_id:
        screen_name = request.user.twitter_id
        tweets = api.user_timeline('@'+screen_name, count=5)
    else:
        screen_name = 'ENews'
        tweets = api.user_timeline('@'+screen_name, count=5)

    header = "Dashboard"
    news = Article.objects.filter(followers=request.user)
    entertainment = Entertainment.objects.filter(followers=request.user)
    data = {
        'tweets': tweets,
        'header': header,
        'screen_name': screen_name,
        'news': news,
        'entertainment': entertainment
        }

    return render(request, 'dashboard.html', data)


@csrf_exempt
@login_required
def twitter(request):
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)
    tweets = ""
    screen_name = ""

    if request.user.twitter_id:
        tweets = api.user_timeline('@jquery', count=10)
        # tweets = api.user_timeline('@'+request.user.twitter_id, count=10)
        screen_name = request.user.twitter_id

    if request.method == 'POST':
        searchTerm = json.loads(request.body)
        tweets = api.user_timeline('@'+searchTerm, count=10)
        screen_name = searchTerm

    data = {'tweets': tweets, 'screen_name': screen_name}
    return render(request, 'twitter.html', data)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/dashboard")
    form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})


@login_required
def preferences(request):
    if request.method == "POST":
        form = PreferencesForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/dashboard")
    form = PreferencesForm(instance=request.user)
    return render(request, 'preferences.html', {'form': form})


@login_required
def favorites(request):
    favorite_news = Article.objects.filter(followers=request.user)
    favorite_entertainment = Entertainment.objects.filter(followers=request.user)

    data = {
        'favorite_news': favorite_news,
        'favorite_entertainment': favorite_entertainment,
    }
    return render(request, 'favorites.html', data)



# Non-visual views; mainly for POST to DB requests
# Should be able to google to see how to have your AJAX queries not be @crsf_exempt
@csrf_exempt
@login_required
def add_favorite_news(request):
    if request.method == "POST":
        favorite_news = json.loads(request.body)
        print favorite_news
        
        # can do article, created = Article.objects.get_or_create instead for readability
        article = Article.objects.get_or_create(
            title=favorite_news['title'],
            abstract=favorite_news['abstract'],
            web_url=favorite_news['web_url'],
            source=NewsSource.objects.get(name=favorite_news['source'])
        )
        article[0].followers.add(request.user)

        if favorite_news['origin'] == '/favorites/':
            return render(request, 'favorites.html')
        else:
            return HttpResponseRedirect('/dashboard')


@csrf_exempt
@login_required
def remove_favorite_news(request):
    if request.method == "POST":
        favorite_news = json.loads(request.body)
        article = Article.objects.get(
            web_url=favorite_news['web_url']
        )
        article.followers.remove(request.user)
        # Article.objects.get(web_url=article.web_url).delete()

        if favorite_news['origin'] == '/favorites/':
            return render(request, 'favorites.html')
        else:
            return HttpResponseRedirect('/dashboard')


@csrf_exempt
@login_required
def add_favorite_entertainment(request):
    if request.method == "POST":
        favorite_entertainment = json.loads(request.body)
        entertainment = Entertainment.objects.get_or_create(
            title=favorite_entertainment['title'],
            url=favorite_entertainment['url'],
            description=favorite_entertainment['description'],
            source=EntertainmentSource.objects.get(name=favorite_entertainment['source'])
        )
        entertainment[0].followers.add(request.user)

        if favorite_entertainment['origin'] == '/favorites/':
            return render(request, 'favorites.html')
        else:
            return HttpResponseRedirect('/dashboard')


@csrf_exempt
@login_required
def remove_favorite_entertainment(request):
    if request.method == "POST":
        favorite_entertainment = json.loads(request.body)
        entertainment = Entertainment.objects.get(
            url=favorite_entertainment['url']
        )
        entertainment.followers.remove(request.user)

        if favorite_entertainment['origin'] == '/favorites/':
            return render(request, 'favorites.html')
        else:
            return HttpResponseRedirect('/dashboard')



# @login_required
# def social_logins(request):
#     if request.method == "POST":
#         form = TwitterForm(request.POST)
#         if form.is_valid():
#             request.user.twitter_id = form.cleaned_data['twitter_handle']
#             request.user.save()
#             redirect("/dashboard")
#     form = TwitterForm()
#     return render(request, 'social_logins.html', {'form': form})



