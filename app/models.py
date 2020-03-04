from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from phone_field import PhoneField

class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        models.Model.__init__(self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class SubCategory(Category):
    class Meta:
        verbose_name_plural = 'Sub-Categories'

class Products(models.Model):
    NAME_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    phone = PhoneField()
    def __str__(self):
        return self.user.username