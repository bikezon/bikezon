from django import forms
from django.contrib.auth.models import User
from app.models import UserProfile
from captcha.fields import ReCaptchaField


class UserForm(forms.ModelForm):
    """ User Form logic
    """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class ReCAPTCHAForm(forms.Form):
    captcha = ReCaptchaField()


class UserProfileForm(forms.ModelForm):
    """ User Profile Form logic - handles
    user profile info, TODO: figure out
    how to display email, username, etc
    """
    class Meta:
        model = UserProfile
        fields = ('stars', 'picture', 'phone')
