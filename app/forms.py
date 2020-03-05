from django import forms
from django.contrib.auth.models import User
from app.models import UserProfile, Product
from captcha.fields import ReCaptchaField
from django.core.files.images import get_image_dimensions


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


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('subcategory', 'name', 'description', 'picture')

    def clean_picture(self):
        avatar = self.cleaned_data['picture']

        try:
            w, h = get_image_dimensions(avatar)

            # validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            # validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image.')

            # validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20kb.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar
