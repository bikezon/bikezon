from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

NAME_MAX_LENGTH = 128


class Category(models.Model):
    """main category for the product, e.g bike, component, etc
    names have to be unique
    """
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
    """subcats are lower level categories, e.g mountain
    bikes, road bikes, handle etc.
    names have to be unique
    """
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'SubCategories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """product model handles all of the products
    that can be registered on site. Seller is the
    person that sells the product. 
    """
    subcategory = models.ManyToManyField("Subcategory")
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    slug = models.SlugField()

    description = models.TextField()
    picture = models.ImageField(
        upload_to='media/product_images/', blank=True)
    dateAdded = models.DateTimeField(default=datetime.now, blank=True)
    views = models.IntegerField(default=0)
    available = models.PositiveSmallIntegerField(default=1)
    price = models.PositiveIntegerField()
    seller = models.ForeignKey(
        "UserProfile", on_delete=models.CASCADE, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductList(models.Model):
    """product list is how wish lists are
    implemented. Wish list has to be created
    automatically on user registration for that user.
    If baskets are implemented, then these also have
    to be created for user automatically on registration.
    """
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    product = models.ManyToManyField("Product")
    item = models.PositiveSmallIntegerField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductList, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Rating(models.Model):
    """Rating can be assigned to products and profiles
    """
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
    """custom UserProfile model that uses django User auth.
    Picture has to have a default. Follows is who this user
    is following.
    """
    # User class implements email, username and password
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(
        upload_to='media/profile_images', default='default.png', blank=True)
    phone = PhoneField(unique=True, blank=True)
    address = models.CharField(max_length=200)
    stars = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True,
        null=True
    )
    follows = models.ManyToManyField('UserProfile', related_name='followed_by')

    def __str__(self):
        return self.user.username
