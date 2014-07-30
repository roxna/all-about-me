import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from allaboutme.settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_SECRET, \
    TWITTER_ACCESS_TOKEN
from news.forms import LoginForm, RegistrationForm, PreferencesForm, TwitterForm
from news.models import *
import tweepy

# Create your views here.


def home(request):
    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            if register_form.save():
                return redirect("profile")

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
    data = {
        'tweets': tweets,
        'header': header,
        'screen_name': screen_name,
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
        tweets = api.user_timeline('@'+request.user.twitter_id, count=10)
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
        form = PreferencesForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/dashboard")
    form = PreferencesForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})


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



