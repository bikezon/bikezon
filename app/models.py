from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'SubCategories'

    def __str__(self):
        return self.name


class Product(models.Model):
    NAME_MAX_LENGTH = 128

    subcategory = models.ManyToManyField("Subcategory")
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    slug = models.SlugField(unique=True)

    description = models.TextField()
    picture = models.ImageField(upload_to='media/product_images/')
    dateAdded = models.DateTimeField(default=datetime.now, blank=True)
    views = models.IntegerField(default=0)
    available = models.PositiveSmallIntegerField(default=1)
    seller = models.ForeignKey(
        "UserProfile", on_delete=models.CASCADE, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductList(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    product = models.ManyToManyField("Product")
    item = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MaxValueValidator(5.0),
            MinValueValidator(1.0)
        ]
    )

    def __str__(self):
        return self.user + self.product


class UserProfile(models.Model):
    # User class implements email, username and password
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='media/profile_images', blank=True)
    phone = PhoneField(unique=True, blank=False)
    address = models.CharField(max_length=200)
    stars = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True
    )

    def __str__(self):
        return self.user.username
