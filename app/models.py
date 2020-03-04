from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.core.validators import MaxValueValidator, MinValueValidator


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
    picture = models.ImageField(upload_to='product_images', blank=False)
    dateAdded = models.DateTimeField(auto_now=False, auto_now_add=False)
    views = models.IntegerField(default=0)
    available = models.PositiveSmallIntegerField()

    seller = models.ForeignKey("UserProfile", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        models.Model.__init__(self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
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
    picture = models.ImageField(upload_to='profile_images', blank=True)
    phone = PhoneField()
    address = models.CharField(max_length=200)
    stars = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True
    )

    def __str__(self):
        return self.user.username
