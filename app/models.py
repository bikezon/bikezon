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

class Subcategory(Category):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Sub-Categories'

class Product(models.Model):
    NAME_MAX_LENGTH = 128

    subcategory = models.ManyToManyField("Subcategory")
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    slug = models.SlugField(unique=True)

    description = models.TextField()
    dateAdded = models.DateTimeField(auto_now=False, auto_now_add=False)
    views = models.IntegerField(default=0)
    available = models.PositiveSmallIntegerField()
    
    seller = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        models.Model.__init__(self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class List(models.Model):
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
    rating = models.DecimalField(max_value=5.00, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.user + self.product

class UserProfile(models.Model):
    #User class implements email, username and password
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    phone = PhoneField()
    address = models.CharField(max_length=200)
    rating = models.DecimalField(max_value=5.00, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.user.username