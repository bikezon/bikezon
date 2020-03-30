from django.contrib import admin
from app.models import Category, UserProfile, Rating, ProductList, Product, \
    SubCategory


class CategoryAdmin(admin.ModelAdmin):
    """admin view for categories, displays
    the name and description of the category
    """
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'description')


class ProductAdmin(admin.ModelAdmin):
    """admin view for products, prepopulates slugs,
    displays name, description, date added, price
    and the seller
    """
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'description', 'dateAdded', 'price', 'seller')


class ProductListAdmin(admin.ModelAdmin):
    """admin view for product lists (e.g wish list),
    prepopulates slug, displays the name, the user
    to whom the list belongs and the products on the
    list.
    """
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'user', 'product')


admin.site.register(Rating)
admin.site.register(SubCategory)
admin.site.register(ProductList, ProductListAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
