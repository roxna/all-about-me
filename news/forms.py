from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from news.models import Person, NewsSource, Article, Social, Entertainment

__author__ = 'roxnairani'


class LoginForm(AuthenticationForm):
        username = forms.CharField(max_length=254,
                                   required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
        password = forms.CharField(required=True,
                                   widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))


class RegistrationForm(UserCreationForm):
        name = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}))
        username = forms.CharField(required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
        email = forms.EmailField(required=True,
                                widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'}))
        password1 = forms.CharField(required=True,
                                    widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
        password2 = forms.CharField(required=True,
                                    widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))

        class Meta:
            model = Person
            fields = ("name", "username", "email", "password1", "password2")

        def clean_username(self):
            username = self.cleaned_data["username"]
            try:
                Person.objects.get(username=username)
            except Person.DoesNotExist:
                return username
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            )


class PreferencesForm(forms.ModelForm):
    twitter_id = forms.CharField(label='Twitter Handle @',
                                widget=forms.TextInput(attrs={'class': 'form-control'}),
                                required=False)
    social_preferences = forms.ModelMultipleChoiceField(queryset=Social.objects.all(),
                                                    label="SOCIAL WEBSITES",
                                                    # help_text="Select the social websites you want to keep track of.",
                                                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-inline'}),
                                                    required=False)
    news_preferences = forms.ModelMultipleChoiceField(queryset=NewsSource.objects.all(),
                                                  label="NEWS WEBSITES",
                                                  # help_text="Select the news websites you would like to follow.",
                                                  widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-inline'}),
                                                  required=False)
    entertainment_preferences = forms.ModelMultipleChoiceField(queryset=Entertainment.objects.all(),
                                                    label="ENTERTAINMENT WEBSITES",
                                                    # help_text="Select the entertainment websites you like to crack up to.",
                                                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-inline'}),
                                                    required=False)

    class Meta:
        model = Person
        fields = ['name', 'email', 'social_preferences', 'twitter_id', 'news_preferences', 'entertainment_preferences']


class TwitterForm(forms.Form):
    twitter_handle = forms.CharField()