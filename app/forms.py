from django import forms
from django.contrib.auth.models import User
from app.models import UserProfile, Product, SubCategory, ProductList
from captcha.fields import ReCaptchaField
from django.core.files.images import get_image_dimensions
from django.db.utils import OperationalError
from phone_field import PhoneField
import logging
import os

# ----------- Logger config ----------- #
if not os.path.exists("logs/"):
    os.makedirs("logs")

if not os.path.exists("logs/main_logs.log"):
    open("logs/main_logs.log", 'a').close()

logger = logging.getLogger(__name__)
logging.basicConfig(filename="logs/main_logs.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


# ----------- Forms ----------- #

class UserForm(forms.ModelForm):
    """ User Form logic
    """
    logger.info("User form hit")
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
        logger.info("Verify password cleaner")
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("verify_password")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                ('Password mismatch.'),
                code='password_mismatch',
            )
        return password2


class ReCAPTCHAForm(forms.Form):
    logger.info("ReCAPTCHA form hit")
    captcha = ReCaptchaField()


class EditProfileForm(forms.ModelForm):
    address = forms.CharField(required=False)
    phone = PhoneField(blank=True, help_text='Contact phone number')

    class Meta:
        model = UserProfile
        fields = ('picture', 'address', 'phone')


class EditListingForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'subcategory', 'price', 'picture')

class UserProfileForm(forms.ModelForm):
    """ User Profile Form logic - handles
    user profile info
    """
    logger.info("User profile form hit")

    class Meta:
        model = UserProfile
        fields = ('picture', 'phone')


class ProductForm(forms.ModelForm):
    logger.info("Product form hit")
    try:
        subcats = SubCategory.objects.values('name')
        subcats = [d['name'] for d in subcats]
        CHOICES = [(subcat[0], subcat) for subcat in subcats]
        subcategory = forms.ChoiceField(
            choices=CHOICES, widget=forms.RadioSelect)
        logger.info("Subcats init success")
    except OperationalError:
        logger.warning("Product form skipped subcats due to db init.")
        pass

    class Meta:
        model = Product
        fields = ('name', 'description', 'subcategory', 'price', 'picture')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = Product.objects.none()

    def clean_picture(self):
        logger.info("Product form cleaning picture")
        avatar = self.cleaned_data['picture']

        try:
            w, h = get_image_dimensions(avatar)

            # validate dimensions
            logger.info("Product form image validate dimensions")
            max_width = max_height = 250
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))
                logger.warning("Product form image bad dimensions")

            # validate content type
            logger.info("Product form image validate content")
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image.')
                logger.warning("Product form image bad content")

            # validate file size
            logger.info("Product form image validate file size")
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20kb.')
                logger.warning("Product form image bad file size")

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            logger.info("Product form no image supplied")
            pass

        return avatar
