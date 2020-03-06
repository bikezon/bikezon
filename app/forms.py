from django import forms
from django.contrib.auth.models import User
from app.models import UserProfile, Product, SubCategory
from captcha.fields import ReCaptchaField
from django.core.files.images import get_image_dimensions


class UserForm(forms.ModelForm):
    """ User Form logic
    """
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control input-lg"}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control input-lg"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control input-lg"}))
    verify_password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control input-lg", "placeholder": "Re-enter password"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def clean_verify_password(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("verify_password")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                ('Password mismatch.'),
                code='password_mismatch',
            )
        return password2


class ReCAPTCHAForm(forms.Form):
    captcha = ReCaptchaField()


class UserProfileForm(forms.ModelForm):
    """ User Profile Form logic - handles
    user profile info, TODO: figure out
    how to display email, username, etc
    """
    class Meta:
        model = UserProfile
        fields = ('picture', 'phone')


class ProductForm(forms.ModelForm):
    subcats = SubCategory.objects.values('name')
    subcats = [d['name'] for d in subcats]
    CHOICES = [(subcat[0], subcat) for subcat in subcats]
    subcategory = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Product
        fields = ('name', 'description', 'subcategory', 'picture')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = Product.objects.none()

    def clean_picture(self):
        avatar = self.cleaned_data['picture']

        try:
            w, h = get_image_dimensions(avatar)

            # validate dimensions
            max_width = max_height = 250
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
